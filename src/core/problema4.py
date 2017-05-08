# -*- coding: utf-8 -*-

import simpy, scipy, numpy, random

from src.core.linear_congruential_generator import LinearCongruentialGenerator

RANDOM_SEED = 42
PT_MEAN = 10.0
PT_SIGMA = 2.0
MTTF_UNIFORM = 10
MTTF_EXPONENTIAL = 20
BREAK_MEAN = 1 / (MTTF_UNIFORM + MTTF_EXPONENTIAL)
NUM_COMPONENTES_INDEPENDENTES = 2
QUANTIDADE_TESTES = 5
SIM_TIME = 7 * 24
UMA_SEMANA = 7 * 24

def tef_uniform():
    """return a random value from uniform distribuition"""
    return scipy.random.uniform(0.0, 8.0)  # hours


def tef_expo():
    """return a random value from exponential distribuition"""
    return scipy.random.standard_exponential(10)  # hours


def time_per_working_part():
    """Return actual processing time for a concrete part."""
    return random.normalvariate(PT_MEAN, PT_SIGMA)


def time_to_failure(componente_id):
    """Return time until next failure for a machine."""
    if componente_id == 1:
        return tef_uniform()  # TEF COMPONENTE A
    elif componente_id == 2:
        return random.expovariate(10)  # TEF COMPONENTE B


def calcular_z(r1, r2):
    return numpy.sqrt(-2 * numpy.log(r1)) * numpy.sin(2 * 180 * r2) + numpy.random.randint(8, 10)


class EquipamentoDoisComponentesIndependentes(object):
    def __init__(self, env, name, repairman):
        self.env = env
        self.name = name
        self.quantidade_de_falhas = 0
        self.broken = False
        self.componente_A = 1
        self.componente_B = 2

        # Start "working" and "break_machine" processes for this machine.
        self.process = env.process(self.working(repairman))

        env.process(self.break_machine(self.componente_A))
        env.process(self.break_machine(self.componente_B))

    def working(self, repairman):
        lcg = LinearCongruentialGenerator()

        while True:
            r1 = lcg.generate_random_numbers(1).pop()
            r2 = lcg.generate_random_numbers(1, initial_seed=r1).pop() + 10
            done_in = abs(calcular_z(r1, r2))

            while done_in:
                try:
                    start = self.env.now
                    yield self.env.timeout(done_in)
                    done_in = 0

                except simpy.Interrupt:
                    self.broken = True
                    done_in -= self.env.now - start  # How much time left?

                    # Request a repairman. This will preempt its "other_job".
                    with repairman.request(priority=10) as req:
                        yield req
                        yield self.env.timeout(time_per_working_part())

                    self.broken = False

            self.quantidade_de_falhas += 1

    def break_machine(self, componente_id):
        """Break the machine every now and then."""
        while True:
            yield self.env.timeout(time_to_failure(componente_id))
            if not self.broken:
                # Only break the machine if it is currently working.
                self.process.interrupt()


def job_equipamento_funcional(env, equipamento_funcionando):
    """The repairman's other (unimportant) job."""
    while True:
        # Start a new job
        done_in = time_per_working_part()
        while done_in:
            with equipamento_funcionando.request(priority=1) as req:
                yield req
                try:
                    start = env.now
                    yield env.timeout(done_in)
                    done_in = 0
                except simpy.Interrupt:
                    done_in -= env.now - start

# Analyis/results
print('Equipamento - 2 Componentes Independentes\n')

print('Resultados depois de %s testes, cada teste de 1 semana (em horas).\n' % QUANTIDADE_TESTES)

for teste_semanal in range(QUANTIDADE_TESTES):
    # Setup and start the simulation
    random.seed(RANDOM_SEED)  # This helps reproducing the results

    # Create an environment and start the setup process
    env = simpy.Environment()
    equipamento_funcionando = simpy.PreemptiveResource(env, capacity=1)

    equipamento = EquipamentoDoisComponentesIndependentes(env, 'Equipamento %d', equipamento_funcionando)

    env.process(job_equipamento_funcional(env, equipamento_funcionando))

    # Execute!
    env.run(until=SIM_TIME)

    print('%s no teste nro %d executou 7 [dias] * 24 [horas] {= %d horas}, falhou %d [vezes].\n' %
          (equipamento.name, teste_semanal, UMA_SEMANA, equipamento.quantidade_de_falhas))
