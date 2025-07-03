# import csv
# from entidades import *


# class SistemaAnaliseEngajamento:
#     VERSAO_ANALISE: str = "2.0"
#     id_plataforma_atual: int = 0

#     def __init__(self):
#         self.__plataformas_registradas: dict[Plataforma] = {}
#         self.__conteudos_registrados: dict[Conteudo]= {}
#         self.__usuarios_registrados: dict[Usuario]= {}
#         self.__proximo_id_plataforma = SistemaAnaliseEngajamento.id_plataforma_atual + 1
#         SistemaAnaliseEngajamento.id_plataforma_atual += 1

#     def cadastrar_plataforma(self, nome: str) -> Plataforma:
#         if nome not in self.__plataformas_registradas:
#             plataforma = Plataforma(nome, self.__proximo_id_plataforma)
#             self.__plataformas_registradas[nome] = plataforma
#             self.__proximo_id_plataforma += 1
#         return self.__plataformas_registradas[nome]

#     def obter_plataforma(self, nome: str) -> Plataforma | None:
#         return self.__plataformas_registradas.get(nome) or None

#     def listar_plataformas(self) -> list[Plataforma]:
#         return list(self.__plataformas_registradas.values())

#     def _carregar_interacoes_csv(self, path: str) -> list[dict]:
#         with open(path, encoding="utf-8") as f:
#             return list(csv.DictReader(f))

#     def processar_interacoes_do_csv(self, path: str):
#         interacoes = self._carregar_interacoes_csv(path)
#         for linha in interacoes:
#             if self.obter_plataforma(linha["plataforma"]) is None:
#                 self.cadastrar_plataforma(linha["plataforma"])

#             if self.__conteudos_registrados.get(linha["id_conteudo"]) is None:
#                 if linha["nome_conteudo"].lower().find("podcast"):
#                     podcast = Podcast(
#                         linha["id_conteudo"],
#                         linha["nome_conteudo"],
#                         linha["watch_duration_seconds"],
#                     )
#                     self.__conteudos_registrados[linha["id_conteudo"]] = podcast
#                 if linha["nome_conteudo"].lower().find("video"):
#                     video = Video(
#                         linha["id_conteudo"],
#                         linha["nome_conteudo"],
#                         linha["watch_duration_seconds"],
#                     )
#                     self.__conteudos_registrados[linha["id_conteudo"]] = video

#                 if linha["nome_conteudo"].lower().find("artigo"):
#                     artigo = Artigo(
#                         linha["id_conteudo"],
#                         linha["nome_conteudo"],
#                         linha["watch_duration_seconds"],
#                     )
#                     self.__conteudos_registrados[linha["id_conteudo"]] = artigo

#             if self.__usuarios_registrados.get(linha["id_usuario"]) is None:
#                 usuario = Usuario(linha["id_usuario"])
#                 self.__usuarios_registrados[linha["id_usuario"]] = usuario

#             try:
#                 plataforma: Plataforma = self.obter_plataforma(linha["plataforma"])
#                 conteudo: Conteudo = self.__conteudos_registrados.get(linha["id_conteudo"])
#                 usuario: Usuario = self.__usuarios_registrados.get(linha["id_usuario"])

#                 try: 
#                     interacao = Interacao(conteudo, plataforma, linha)
#                 except ValueError as e:
#                     print(f"Erro ao criar interação: {e}")
#                     continue
                    
#                 try:
#                     conteudo.adicionar_interacao(interacao)
#                 except ValueError as e:
#                     print(f"Erro ao adicionar interação ao conteúdo: {e}")
#                     continue
                
#                 try:
#                     usuario.registrar_interacao(interacao)
#                 except ValueError as e:
#                     print(f"Erro ao registrar interação no usuário: {e}")
#                     continue
            
#             except ValueError as e:
#                 print(f"Erro ao processar interação: {e}")

#     def gerar_relatorio_engajamento_conteudos(self):

#         for conteudo in self.__conteudos_registrados.values():
#             print(f"\nConteúdo: {conteudo}")
#             print("- Total de interações de engajamento:")
#             print(f"  • {conteudo.calcular_total_interacoes_engajamento()}")

#             print("- Contagem por tipo de interação:")
#             contagem = conteudo.calcular_contagem_por_tipo_interacao()
#             for tipo, qtd in contagem.items():
#                 print(f"  • {tipo}: {qtd}")

                

#     def gerar_relatorio_atividade_usuarios(self):
#         print("Chamando métodos da classe Usuario")

#         for usuario in self.__usuarios_registrados.values():
#             print(f"\nUsuário: {usuario}")

#             for interacao in usuario._interacoes_realizadas:
#                 print("- Interações do tipo 'like':")
#                 likes = usuario.obter_interacoes_por_tipo('like')
#                 if not likes:
#                     print("  • Nenhum like registrado.")
#                 else:
#                     for like in likes:
#                         print(f"  • {like}")

#                 print("- Interações do tipo 'comment':")
#                 comments = usuario.obter_interacoes_por_tipo('comment')
#                 if not comments:
#                     print("  • Nenhum comentário registrado.")
#                 else:
#                     for comment in comments:
#                         print(f"  • {comment}")

#                 print("- Interações do tipo 'share':")
#                 shares = usuario.obter_interacoes_por_tipo('share')
#                 if not shares:
#                     print("  • Nenhum compartilhamento registrado.")
#                 else:
#                     for share in shares:
#                         print(f"  • {share}")
                        

#                 print("- Interações do tipo 'view_start':")
#                 views_starts = usuario.obter_interacoes_por_tipo('view_start')
#                 if not views_starts:   
#                     print("  • Nenhuma visualização registrada.")
#                 else:
#                     for view_start in views_starts:
#                         print(f"  • {view_start}")
#                 print()

#                 print("- Conteúdos únicos consumidos:")
#                 for conteudo in usuario.obter_conteudos_unicos_consumidos():
#                     print(f"  • {conteudo}")
#                 print()

#                 print("- Tempo total de consumo por plataforma:")
#                 for plataforma in self.__plataformas_registradas.values():
#                     tempo = usuario.calcular_tempo_total_consumo_plataforma(plataforma)
#                     print(f"  • {plataforma}: {tempo} segundos")
#                 print()

#                 print("- Plataformas mais frequentes - Top 3:")
#                 for plataforma, valor in usuario.plataformas_mais_frequentes(3) :
#                     print(f"  • {plataforma}: {valor} vez(es)")
#                 print()

#     def identificar_top_conteudos(self, metrica, top_n=3):
#         if metrica not in ['tempo_total_consumo', 'percentual_medio_assistido', 'media_tempo_consumo']:
#             raise ValueError("Métrica inválida. Use 'tempo_total_consumo', 'percentual_medio_assistido' ou 'media_tempo_consumo'.")        
        
#         if metrica == 'tempo_total_consumo':           
#             for conteudo in self.__conteudos_registrados.values():
#                 print(f"- {conteudo.nome_conteudo}:")
#                 print(f"  • {conteudo.calcular_tempo_total_consumo()} segundos")
#                 conteudos = sorted(
#                     self.__conteudos_registrados.values(),
#                     key=lambda c: c.calcular_tempo_total_consumo(),
#                     reverse=True
#                 )
#             return conteudos[:top_n]
        

#         if metrica == 'media_tempo_consumo':
#             for conteudo in self.__conteudos_registrados.values():
#                 print(f"- {conteudo.nome_conteudo}:")
#                 print(f"  • {conteudo.calcular_media_tempo_consumo():.2f} segundos")
#                 conteudos = sorted(
#                     self.__conteudos_registrados.values(),
#                     key=lambda c: c.calcular_media_tempo_consumo(),
#                     reverse=True
#                 )
#             return conteudos[:top_n]

        


import csv
from typing import List

# Importações das estruturas de dados e entidades
from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca
from entidades.plataforma import Plataforma
from entidades.conteudo.conteudo import Conteudo
from entidades.conteudo.video import Video
from entidades.conteudo.podcast import Podcast
from entidades.conteudo.artigo import Artigo
from entidades.usuario import Usuario
from entidades.interacao import Interacao

# Importação do algoritmo de ordenação
from analise.algoritmos import quick_sort

class SistemaAnaliseEngajamento:
    """
    Classe orquestradora que gerencia a análise de engajamento, utilizando
    Fila para processamento de dados e Árvores de Busca Binária para
    armazenamento e busca eficiente de conteúdos e usuários.
    """
    def __init__(self):
        # Fila para processar as interações brutas do CSV
        self._fila_interacoes_brutas = Fila()
        
        # Árvores de Busca Binária para gerenciamento eficiente
        self._arvore_conteudos = ArvoreBinariaBusca()
        self._arvore_usuarios = ArvoreBinariaBusca()
        
        # Dicionário para plataformas, pois a busca por nome é mais direta
        self._plataformas_registradas = {}

    def _carregar_interacoes_csv(self, caminho_arquivo: str):
        """
        Lê um arquivo CSV e enfileira cada linha para processamento posterior.
        - Complexidade de Tempo: O(M), onde M é o número de linhas no arquivo CSV.
        - Complexidade de Espaço: O(M), pois todas as linhas são armazenadas na fila.
        """
        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
                leitor_csv = csv.DictReader(arquivo)
                for linha in leitor_csv:
                    self._fila_interacoes_brutas.enfileirar(linha)
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'")
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")

    def processar_interacoes_da_fila(self):
        """
        Processa todas as interações da fila, criando e associando objetos.
        - Complexidade de Tempo: O(M * log N), onde M é o número de interações
          e N é o número de conteúdos/usuários únicos. Para cada interação,
          realiza-se uma operação de busca/inserção (log N) na árvore.
        - Complexidade de Espaço: O(N + P), para armazenar N usuários/conteúdos
          e P plataformas.
        """
        while not self._fila_interacoes_brutas.esta_vazia():
            linha_interacao = self._fila_interacoes_brutas.desenfileirar()

            # 1. Gerenciar Plataforma
            nome_plataforma = linha_interacao.get('nome_plataforma', 'desconhecida')
            if nome_plataforma not in self._plataformas_registradas:
                self._plataformas_registradas[nome_plataforma] = Plataforma(nome_plataforma)
            plataforma = self._plataformas_registradas[nome_plataforma]

            # 2. Gerenciar Conteúdo
            id_conteudo = int(linha_interacao.get('id_conteudo', 0))
            conteudo = self._arvore_conteudos.buscar(id_conteudo)
            if not conteudo:
                tipo_conteudo = linha_interacao.get('tipo_conteudo', 'desconhecido')
                titulo = linha_interacao.get('titulo', 'sem_titulo')
                if tipo_conteudo == 'video':
                    conteudo = Video(id_conteudo, titulo)
                elif tipo_conteudo == 'podcast':
                    conteudo = Podcast(id_conteudo, titulo)
                elif tipo_conteudo == 'artigo':
                    conteudo = Artigo(id_conteudo, titulo)
                else:
                    conteudo = Conteudo(id_conteudo, titulo)
                self._arvore_conteudos.inserir(id_conteudo, conteudo)

            # 3. Gerenciar Usuário
            id_usuario = int(linha_interacao.get('id_usuario', 0))
            usuario = self._arvore_usuarios.buscar(id_usuario)
            if not usuario:
                usuario = Usuario(id_usuario)
                self._arvore_usuarios.inserir(id_usuario, usuario)

            # 4. Criar e Registrar Interação
            try:
                interacao = Interacao(linha_interacao, conteudo, plataforma)
                conteudo.adicionar_interacao(interacao)
                usuario.adicionar_interacao(interacao)
                plataforma.adicionar_interacao(interacao)
            except (ValueError, TypeError) as e:
                print(f"Erro ao processar interação para o conteúdo {id_conteudo}: {e}")

    def pipeline_completo(self, caminho_arquivo: str):
        """Executa o pipeline completo: carregar, processar e gerar relatórios."""
        print("************ Iniciando pipeline completo ************\n")
        print("1. Carregando interações do CSV para a fila...")
        self._carregar_interacoes_csv(caminho_arquivo)
        print("-> Carga finalizada.\n")

        print("2. Processando interações da fila...")
        self.processar_interacoes_da_fila()
        print("-> Processamento finalizado.\n")

        print("3. Gerando relatórios de análise...")
        self.gerar_todos_os_relatorios()
        print("\n************ Pipeline finalizado ************")

    def gerar_todos_os_relatorios(self, top_n: int = 5):
        """Agrupa a chamada de todos os relatórios solicitados no projeto."""
        print("\n--- RELATÓRIOS DE ENGAJAMENTO GLOBO ---")
        self.identificar_top_conteudos_por_consumo(top_n)
        self.identificar_top_usuarios_por_consumo(top_n)
        self.identificar_plataformas_por_engajamento()
        self.identificar_top_conteudos_por_comentarios(top_n)
        self.identificar_top_conteudos_por_interacoes(top_n)
        self.calcular_tempo_medio_por_plataforma()

    def identificar_top_conteudos_por_consumo(self, top_n: int = 5):
        """
        Relatório 7.1: Ranking de conteúdos mais consumidos.
        - Complexidade de Tempo: O(N log N) - Dominado pela ordenação.
        - Complexidade de Espaço: O(N) - Para a lista de conteúdos.
        """
        print(f"\n--- Top {top_n} Conteúdos por Tempo Total de Consumo ---")
        todos_conteudos = self._arvore_conteudos.percurso_em_ordem()
        conteudos_ordenados = quick_sort(
            todos_conteudos, 
            key=lambda c: c.calcular_tempo_total_consumo(), 
            reverse=True
        )
        for i, conteudo in enumerate(conteudos_ordenados[:top_n]):
            print(f"{i+1}. ID:{conteudo.id_conteudo} | Título: '{conteudo.titulo}' | Tempo: {conteudo.calcular_tempo_total_consumo()}s")

    def identificar_top_usuarios_por_consumo(self, top_n: int = 5):
        """
        Relatório 7.2: Usuários com maior tempo total de consumo.
        - Complexidade de Tempo: O(U log U) - Dominado pela ordenação (U = num usuários).
        - Complexidade de Espaço: O(U) - Para a lista de usuários.
        """
        print(f"\n--- Top {top_n} Usuários por Tempo Total de Consumo ---")
        todos_usuarios = self._arvore_usuarios.percurso_em_ordem()
        usuarios_ordenados = quick_sort(
            todos_usuarios,
            key=lambda u: u.calcular_tempo_total_consumo(),
            reverse=True
        )
        for i, usuario in enumerate(usuarios_ordenados[:top_n]):
            print(f"{i+1}. ID Usuário: {usuario.id_usuario} | Tempo Total Consumido: {usuario.calcular_tempo_total_consumo()}s")

    def identificar_plataformas_por_engajamento(self):
        """
        Relatório 7.3: Plataforma com maior engajamento.
        - Complexidade de Tempo: O(P log P) - Dominado pela ordenação (P = num plataformas).
        - Complexidade de Espaço: O(P) - Para a lista de plataformas.
        """
        print("\n--- Ranking de Plataformas por Engajamento (likes, shares, comments) ---")
        lista_plataformas = list(self._plataformas_registradas.values())
        plataformas_ordenadas = quick_sort(
            lista_plataformas,
            key=lambda p: p.calcular_total_interacoes_engajamento(),
            reverse=True
        )
        for i, plataforma in enumerate(plataformas_ordenadas):
            print(f"{i+1}. Plataforma: {plataforma.nome} | Interações de Engajamento: {plataforma.calcular_total_interacoes_engajamento()}")

    def identificar_top_conteudos_por_comentarios(self, top_n: int = 5):
        """
        Relatório 7.4: Conteúdos mais comentados.
        - Complexidade de Tempo: O(N log N) - Dominado pela ordenação.
        - Complexidade de Espaço: O(N) - Para a lista de conteúdos.
        """
        print(f"\n--- Top {top_n} Conteúdos por Número de Comentários ---")
        todos_conteudos = self._arvore_conteudos.percurso_em_ordem()
        conteudos_ordenados = quick_sort(
            todos_conteudos,
            key=lambda c: c.calcular_metricas()['comment'],
            reverse=True
        )
        for i, conteudo in enumerate(conteudos_ordenados[:top_n]):
            print(f"{i+1}. ID:{conteudo.id_conteudo} | Título: '{conteudo.titulo}' | Comentários: {conteudo.calcular_metricas()['comment']}")
            
    def identificar_top_conteudos_por_interacoes(self, top_n: int = 5):
        """
        Relatório 7.5: Total de interações por tipo de conteúdo.
        - Complexidade de Tempo: O(N log N) - Dominado pela ordenação.
        - Complexidade de Espaço: O(N) - Para a lista de conteúdos.
        """
        print(f"\n--- Top {top_n} Conteúdos por Quantidade Total de Interações ---")
        todos_conteudos = self._arvore_conteudos.percurso_em_ordem()
        conteudos_ordenados = quick_sort(
            todos_conteudos,
            key=lambda c: len(c.interacoes),
            reverse=True
        )
        for i, conteudo in enumerate(conteudos_ordenados[:top_n]):
            print(f"{i+1}. ID:{conteudo.id_conteudo} | Tipo: {conteudo.__class__.__name__} | Título: '{conteudo.titulo}' | Total de Interações: {len(conteudo.interacoes)}")

    def calcular_tempo_medio_por_plataforma(self):
        """
        Relatório 7.6: Tempo médio de consumo para cada tipo de plataforma.
        - Complexidade de Tempo: O(P) - Itera sobre as plataformas.
        - Complexidade de Espaço: O(1).
        """
        print("\n--- Tempo Médio de Consumo por Plataforma ---")
        for nome, plataforma in self._plataformas_registradas.items():
            tempo_medio = plataforma.calcular_tempo_medio_consumo()
            print(f"- Plataforma: {nome} | Tempo Médio: {tempo_medio:.2f}s")
