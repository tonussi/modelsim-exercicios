# -*- coding: utf-8 -*-

import simpy, scipy, numpy, random

from src.core.linear_congruential_generator import LinearCongruentialGenerator

RANDOM_SEED = 42
NUM_COMPONENTES_INDEPENDENTES = 2
QUANTIDADE_TESTES = 5
TEMPO_SIMULACAO = 7 * 24

def tef_uniform():
    """return a random value from uniform distribuition"""
    return scipy.random.uniform(0.0, 8.0)  # hours


def tef_expo():
    """return a random value from exponential distribuition"""
    return scipy.random.standard_exponential(10)  # hours


def tempo_do_equipamento_funcionando():
    """Return actual processing time for a concrete part."""
    return random.normalvariate(10.0, 2.0)


def tef(componente_id):
    """Return time until next failure for a machine."""
    if componente_id == 1:
        return tef_uniform()  # TEF COMPONENTE A
    elif componente_id == 2:
        return random.expovariate(10)  # TEF COMPONENTE B


def calcular_z(r1, r2):
    return numpy.sqrt(-2 * numpy.log(r1)) * numpy.sin(2 * 180 * r2) + numpy.random.randint(8, 10)


class EquipamentoDoisComponentesIndependentes(object):
    def __init__(self, env, name, equipamento_funcionando):
        self.env = env
        self.name = name
        self.tempo_entre_falhas_total = 0
        self.broken = False
        self.componente_A = 1
        self.componente_B = 2

        # Start "working" and "break_machine" processes for this machine.
        self.process = env.process(self.working(equipamento_funcionando))

        env.process(self.break_machine(self.componente_A))
        env.process(self.break_machine(self.componente_B))

    def working(self, reparador_de_componente):
        lcg = LinearCongruentialGenerator()

        while True:

            r1 = lcg.generate_random_numbers(1).pop()
            r2 = lcg.generate_random_numbers(1, initial_seed=r1).pop() + 10

            # Gero um x aleatorio usando o Linear Congruential Generator
            done_in = abs(calcular_z(r1, r2))

            # Espero um componente voltar do tempo falhando (simulacao desse evento, periodo falhando, evento)
            while done_in:

                try:
                    start = self.env.now
                    yield self.env.timeout(done_in)
                    done_in = 0

                except simpy.Interrupt:
                    self.broken = True
                    done_in -= self.env.now - start

                    # Salva o tempo em que o componente esteve falhando
                    self.tempo_entre_falhas_total += done_in

                    # Chama um reparador de componente para faze voltar a funcionar
                    with reparador_de_componente.request(priority=1) as req:
                        yield req
                        yield self.env.timeout(tempo_do_equipamento_funcionando())
                    self.broken = False

    def break_machine(self, componente_id):

        # Funcao de quebra de componente
        # a funcao tef sendo chamada abaixo leva em consideracao o tipo de componente
        # se for o componente que segue uma distribuicao uniforme em horas vai ser usado tef_uniform para esse componente
        # do contrario vai ser usado tef_expo para o outro componente do equipamento

        while True:
            yield self.env.timeout(tef(componente_id))
            if not self.broken:
                # Only break the machine if it is currently working.
                self.process.interrupt()

# Analyis/results
print('Equipamento - 2 Componentes Independentes\n')

print('Resultados depois de %s testes, cada teste de 1 semana (em horas).\n' % QUANTIDADE_TESTES)

media_tempo_falhas = 0

for teste_semanal in range(QUANTIDADE_TESTES):
    # Setup and start the simulation
    random.seed(RANDOM_SEED)  # This helps reproducing the results

    # Create an environment and start the setup process
    env = simpy.Environment()
    equipamento_funcionando = simpy.PreemptiveResource(env, capacity=1)

    equipamento = EquipamentoDoisComponentesIndependentes(env, 'Equipamento %d', equipamento_funcionando)

    # Execute!
    env.run(until=TEMPO_SIMULACAO)

    print('%s no teste nro %d executou 7 [dias] * 24 [horas] {= %d horas}, falhou %d [horas].\n' %
          (equipamento.name, teste_semanal, TEMPO_SIMULACAO, equipamento.tempo_entre_falhas_total))

    media_tempo_falhas += equipamento.tempo_entre_falhas_total

print('Em media o equipamento falha por %d / semana' % (media_tempo_falhas / QUANTIDADE_TESTES))

#Equipamento - 2 Componentes Independentes
#Resultados depois de 5 testes, cada teste de 1 semana (em horas).
#Equipamento %d no teste nro 0 executou 7 [dias] * 24 [horas] {= 168 horas}, falhou 68 [horas].
#Equipamento %d no teste nro 1 executou 7 [dias] * 24 [horas] {= 168 horas}, falhou 85 [horas].
#Equipamento %d no teste nro 2 executou 7 [dias] * 24 [horas] {= 168 horas}, falhou 64 [horas].
#Equipamento %d no teste nro 3 executou 7 [dias] * 24 [horas] {= 168 horas}, falhou 84 [horas].
#Equipamento %d no teste nro 4 executou 7 [dias] * 24 [horas] {= 168 horas}, falhou 84 [horas].
#Em media o equipamento falha por 77 / semana
#Process finished with exit code 0
