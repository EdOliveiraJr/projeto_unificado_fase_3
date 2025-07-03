# class Conteudo:
#     def __init__(self, id_conteudo, nome_conteudo):
#         # Armazenar o id e o nome do conteúdo
#         self._id_conteudo = id_conteudo
#         self._nome_conteudo = nome_conteudo
#         self._interacoes = []

#     # Property para acessar o id de forma segura
#     @property
#     def id_conteudo(self):
#         return self._id_conteudo

#     @id_conteudo.setter
#     def id_conteudo(self, valor):
#         self._id_conteudo = valor

#     @property
#     def nome_conteudo(self):
#         return self._nome_conteudo

#     @nome_conteudo.setter
#     def nome_conteudo(self, valor):
#         self._nome_conteudo = valor

#     # Interações
#     # Adiciona uma interação à lista de interações
#     def adicionar_interacao(self, interacao):
#         self._interacoes.append(interacao)

#     # Calcula o total de interações de engajamento (like, share, comment)
#     def calcular_total_interacoes_engajamento(self):
#         tipos_engajamento = {"like", "share", "comment"}
#         return sum(
#             1
#             for inter in self._interacoes
#             if getattr(inter, "tipo_interacao", None) in tipos_engajamento
#         )

#     # Conta quantas interações de cada tipo existem
#     def calcular_contagem_por_tipo_interacao(self):
#         contagem = {}
#         for inter in self._interacoes:
#             tipo = getattr(inter, "tipo_interacao", None)
#             if tipo:
#                 contagem[tipo] = contagem.get(tipo, 0) + 1
#         return contagem

#     # Soma o tempo total de consumo (watch_duration_seconds)
#     def calcular_tempo_total_consumo(self):
#         return sum(
#             getattr(inter, "watch_duration_seconds", 0) or 0
#             for inter in self._interacoes
#         )

#     # Calcula a média do tempo de consumo maior que zero
#     def calcular_media_tempo_consumo(self):
#         tempos = [
#             getattr(inter, "watch_duration_seconds", 0) or 0
#             for inter in self._interacoes
#             if getattr(inter, "watch_duration_seconds", 0)
#         ]
#         if tempos:
#             return sum(tempos) / len(tempos)
#         return 0

#     # Retorna uma lista com os textos dos comentários
#     def listar_comentarios(self):
#         return [
#             getattr(inter, "comment_text", "")
#             for inter in self._interacoes
#             if getattr(inter, "tipo_interacao", None) == "comment"
#         ]

#     # Métodos mágicos str e repr
#     # Mostra o nome do conteúdo ao imprimir o objeto
#     def __str__(self):
#         return self._nome_conteudo

#     # Representação para debug
#     def __repr__(self):
#         return f"Conteudo(id={self._id_conteudo}, nome='{self._nome_conteudo}')"


from datetime import datetime

class Conteudo:
    """Classe base para todos os tipos de conteúdo."""
    def __init__(self, id_conteudo: int, titulo: str):
        # O erro 'AttributeError' ocorria porque estes atributos não estavam sendo definidos.
        self._id_conteudo = id_conteudo
        self._titulo = titulo
        self._interacoes = []

    @property
    def id_conteudo(self) -> int:
        return self._id_conteudo

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def interacoes(self) -> list:
        return self._interacoes

    def adicionar_interacao(self, interacao):
        self._interacoes.append(interacao)

    def calcular_total_interacoes_engajamento(self) -> int:
        """Calcula o total de interações que contam como engajamento (like, share, comment)."""
        tipos_engajamento = {'like', 'share', 'comment'}
        return sum(1 for i in self._interacoes if i.tipo_interacao in tipos_engajamento)

    def calcular_tempo_total_consumo(self) -> int:
        """Calcula o tempo total de consumo em segundos."""
        return sum(i.watch_duration_seconds for i in self._interacoes if i.watch_duration_seconds is not None)

    def calcular_metricas(self) -> dict:
        """Calcula e retorna um dicionário com várias métricas de engajamento."""
        metricas = {'like': 0, 'share': 0, 'comment': 0, 'view': 0}
        for interacao in self._interacoes:
            if interacao.tipo_interacao in metricas:
                metricas[interacao.tipo_interacao] += 1
        return metricas

    def __repr__(self):
        return f"Conteudo(ID={self.id_conteudo}, Título='{self.titulo}')"
