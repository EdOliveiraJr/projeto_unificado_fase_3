# import datetime
# from entidades import Conteudo
# from entidades import Plataforma

# class Interacao:

#     def __init__(self, conteudo_associado: Conteudo, plataforma_interacao: Plataforma, linha_csv: dict) -> None:
#         TIPOS_INTERACAO_VALIDOS = ['view_start', 'like', 'share', 'comment']
#         self.__conteudo_associado: Conteudo = conteudo_associado
#         self.__plataforma_interacao: Plataforma = plataforma_interacao
#         self.__id_usuario: int = int(linha_csv['id_usuario'] or 0)
#         self.__timestamp_interacao: datetime.datetime = datetime.datetime.strptime(
#             linha_csv['timestamp_interacao'], "%Y-%m-%d %H:%M:%S"
#         )
#         self.__watch_duration_seconds: int = int(linha_csv['watch_duration_seconds'] or 0)
#         self.__comment_text: str = linha_csv.get('comment_text', '').strip()

#         if linha_csv['tipo_interacao'] in TIPOS_INTERACAO_VALIDOS:
#             self.__tipo_interacao = linha_csv['tipo_interacao']
#         else:
#             self.__tipo_interacao = "Interação inválida"

#         if self.__watch_duration_seconds < 0:
#             self.__watch_duration_seconds = 0

#     def __str__(self):
#         return f"""Conteúdo associado: {self.conteudo_associado}
#         Plataforma de interação: {self.plataforma_interacao}
#         ID usuário: {self.id_usuario}
#         Timestamp da interação: {self.timestamp_interacao}
#         Tipo de interação: {self.tipo_interacao}
#         Watch duration seconds: {self.watch_duration_seconds}
#         Comment text: {self.comment_text}
#         """

#     def __repr__(self):
#         return self.__str__()

#     @property
#     def conteudo_associado(self) -> Conteudo:
#         return self.__conteudo_associado

#     @property
#     def plataforma_interacao(self) -> Plataforma:
#         return self.__plataforma_interacao

#     @property
#     def id_usuario(self) -> int:
#         return self.__id_usuario

#     @property
#     def timestamp_interacao(self) -> datetime.datetime:
#         return self.__timestamp_interacao

#     @property
#     def tipo_interacao(self) -> str:
#         return self.__tipo_interacao

#     @property
#     def watch_duration_seconds(self) -> int:
#         return self.__watch_duration_seconds

#     @property
#     def comment_text(self) -> str:
#         return self.__comment_text


import datetime

# Importações para type hinting
from entidades.conteudo.conteudo import Conteudo
from entidades.plataforma import Plataforma

# CORREÇÃO 1: Adicionado 'view_start' aos tipos válidos para aceitar os dados do CSV.
TIPOS_INTERACAO_VALIDOS = {'view', 'like', 'share', 'comment', 'view_start'}

class Interacao:
    """Representa uma interação de um usuário com um conteúdo em uma plataforma."""

    def __init__(self, linha_csv: dict, conteudo_associado: Conteudo, plataforma_interacao: Plataforma):
        self._conteudo_associado = conteudo_associado
        self._plataforma_interacao = plataforma_interacao
        self._id_usuario = int(linha_csv.get('id_usuario', 0))
        
        try:
            timestamp_str = linha_csv.get('timestamp_interacao', '')
            self._timestamp_interacao = datetime.datetime.fromisoformat(timestamp_str) if timestamp_str else None
        except ValueError:
            self._timestamp_interacao = None

        self._tipo_interacao = linha_csv.get('tipo_interacao', '').strip()
        if self._tipo_interacao not in TIPOS_INTERACAO_VALIDOS:
            raise ValueError(f"Tipo de interação inválido: {self._tipo_interacao}")

        # CORREÇÃO 2: Tratamento para valores vazios em 'watch_duration_seconds'.
        watch_duration_str = linha_csv.get('watch_duration_seconds', '0')
        self._watch_duration_seconds = int(watch_duration_str) if watch_duration_str.isdigit() else 0
        
        self._comment_text = linha_csv.get('comment_text', '').strip()

    @property
    def conteudo_associado(self) -> Conteudo:
        return self._conteudo_associado

    @property
    def plataforma_interacao(self) -> Plataforma:
        return self._plataforma_interacao

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def timestamp_interacao(self) -> datetime.datetime:
        return self._timestamp_interacao

    @property
    def tipo_interacao(self) -> str:
        return self._tipo_interacao

    @property
    def watch_duration_seconds(self) -> int:
        return self._watch_duration_seconds

    @property
    def comment_text(self) -> str:
        return self._comment_text

    def __repr__(self):
        return f"Interacao(Usuario={self.id_usuario}, Tipo='{self.tipo_interacao}', Conteudo_ID={self.conteudo_associado.id_conteudo})"
