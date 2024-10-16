# personal_trainer_prompt.py

def gerar_prompt_personalizado(biotipo, tempo_disponivel, preferencias_exercicios, nivel_experiencia):
    """
    Gera um prompt para um assistente de personal trainer personalizar treinos.

    :param biotipo: Tipo de corpo do usuário (ex: "ectomorfo", "mesomorfo", "endomorfo").
    :param tempo_disponivel: Tempo disponível para treinos por semana (em horas).
    :param preferencias_exercicios: Lista de tipos de exercícios preferidos (ex: ["musculação", "corrida", "yoga"]).
    :param nivel_experiencia: Nível de experiência do usuário (ex: "iniciante", "intermediário", "avançado").
    :return: String contendo o prompt personalizado.
    """
    prompt = f"""
    Você é um assistente de personal trainer. Seu objetivo é criar um plano de treino ideal baseado nas seguintes características do usuário:

    1. **Biotipo Corporal**: {biotipo}
    2. **Disponibilidade de Tempo**: {tempo_disponivel} horas por semana
    3. **Preferências de Exercícios**: {', '.join(preferencias_exercicios)}
    4. **Nível de Experiência**: {nivel_experiencia}

    Com base nas informações acima, crie um plano de treino que inclua:
    - Frequência semanal dos treinos
    - Tipos de exercícios e suas durações
    - Sugestões de aquecimento e alongamento
    - Recomendações de progressão ao longo do tempo, adaptadas ao nível de experiência
    - Ajustes específicos para o biotipo corporal do usuário

    Certifique-se de adaptar o plano às necessidades e limitações físicas do usuário, oferecendo uma evolução segura e eficiente.
    """
    return prompt

# Exemplo de uso
biotipo = "mesomorfo"
tempo_disponivel = 5  # horas por semana
preferencias_exercicios = ["musculação", "corrida"]
nivel_experiencia = "intermediário"

prompt_gerado = gerar_prompt_personalizado(biotipo, tempo_disponivel, preferencias_exercicios, nivel_experiencia)
print(prompt_gerado)
