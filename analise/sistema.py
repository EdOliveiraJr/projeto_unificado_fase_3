import csv
from entidades import *
from estruturas_dados import *
from analise.algoritmos_ordenacao import quick_sort

class SistemaAnaliseEngajamento:
    VERSAO_ANALISE: str = "2.0"
    id_plataforma_atual: int = 0

    def __init__(self):
        self.__plataformas_registradas: dict[Plataforma] = {}
        self.__arvore_conteudos = ArvoreBinariaBusca()
        self.__arvore_usuarios = ArvoreBinariaBusca()
        self.__proximo_id_plataforma = SistemaAnaliseEngajamento.id_plataforma_atual + 1
        self.__fila_interacoes_brutas = Fila()
        SistemaAnaliseEngajamento.id_plataforma_atual += 1

    # Métodos de conteudo a partir da classe arvore_binaria_busca
    def inserir_conteudo(self, conteudo):
        self.__arvore_conteudos.inserir(conteudo._id_conteudo, conteudo)

    def buscar_conteudo(self, id_conteudo):
        return self.__arvore_conteudos.buscar(id_conteudo)

    def remover_conteudo(self, id_conteudo):
        self.__arvore_conteudos.remover(id_conteudo)

    def percurso_em_ordem(self):
        return [valor for chave, valor in self.__arvore_conteudos.percurso_em_ordem()]

    # Métodos de usuario a partir da classe arvore_binaria_busca
    def inserir_usuario(self, usuario):
        self.__arvore_usuarios.inserir(usuario._id_usuario, usuario)

    def buscar_usuario(self, id_usuario):
        return self.__arvore_usuarios.buscar(id_usuario)

    def remover_usuario(self, id_usuario):
        self.__arvore_usuarios.remover(id_usuario)

    def percurso_em_ordem_usuarios(self):
        return [valor for chave, valor in self.__arvore_usuarios.percurso_em_ordem()]

    def cadastrar_plataforma(self, nome: str) -> Plataforma:
        if nome not in self.__plataformas_registradas:
            plataforma = Plataforma(nome, self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome] = plataforma
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome]

    def obter_plataforma(self, nome: str) -> Plataforma | None:
        return self.__plataformas_registradas.get(nome) or None

    def listar_plataformas(self) -> list[Plataforma]:
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, path: str) -> list[dict]:
        with open(path, encoding="utf-8") as f:
            lista = list(csv.DictReader(f))
            for linha in lista:
                self.__fila_interacoes_brutas.enfileirar(linha)

    def processar_interacoes_do_csv(self, path: str):
        self._carregar_interacoes_csv(path)

        while not self.__fila_interacoes_brutas.esta_vazia():
            linha = self.__fila_interacoes_brutas.desenfileirar()

            if self.obter_plataforma(linha["plataforma"]) is None:
                self.cadastrar_plataforma(linha["plataforma"])

            if self.__arvore_conteudos.buscar(linha["id_conteudo"]) is None:
                if linha["nome_conteudo"].lower().find("podcast"):
                    podcast = Podcast(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__arvore_conteudos.inserir(podcast.id_conteudo, podcast)
                if linha["nome_conteudo"].lower().find("video"):
                    video = Video(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__arvore_conteudos.inserir(video.id_conteudo, video)

                if linha["nome_conteudo"].lower().find("artigo"):
                    artigo = Artigo(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__arvore_conteudos.inserir(artigo.id_conteudo, artigo)

            if self.__arvore_usuarios.buscar(linha["id_usuario"]) is None:
                usuario = Usuario(linha["id_usuario"])
                self.__arvore_usuarios.inserir(usuario.id_usuario, usuario)

            try:
                plataforma: Plataforma = self.obter_plataforma(linha["plataforma"])
                conteudo: Conteudo = self.__arvore_conteudos.buscar(
                    linha["id_conteudo"]
                )
                usuario: Usuario = self.__arvore_usuarios.buscar(linha["id_usuario"])

                try:
                    interacao = Interacao(conteudo, plataforma, linha)
                except ValueError as e:
                    print(f"Erro ao criar interação: {e}")
                    continue

                try:
                    conteudo.adicionar_interacao(interacao)
                except ValueError as e:
                    print(f"Erro ao adicionar interação ao conteúdo: {e}")
                    continue

                try:
                    usuario.registrar_interacao(interacao)
                except ValueError as e:
                    print(f"Erro ao registrar interação no usuário: {e}")
                    continue

            except ValueError as e:
                print(f"Erro ao processar interação: {e}")

    def gerar_relatorio_engajamento_conteudos(self):
        for conteudo in self.__arvore_conteudos.percurso_em_ordem():
            print(f"\nConteúdo: {conteudo}")
            print("- Total de interações de engajamento:")
            print(f"  • {conteudo.calcular_total_interacoes_engajamento()}")

            print("- Contagem por tipo de interação:")
            contagem = conteudo.calcular_contagem_por_tipo_interacao()
            for tipo, qtd in contagem.items():
                print(f"  • {tipo}: {qtd}")

    def gerar_relatorio_atividade_usuarios(self):
        print("Chamando métodos da classe Usuario")
        for usuario in self.__arvore_usuarios.percurso_em_ordem():
            print(f"\nUsuário: {usuario}")

            for interacao in usuario._interacoes_realizadas:
                print("- Interações do tipo 'like':")
                likes = usuario.obter_interacoes_por_tipo("like")
                if not likes:
                    print("  • Nenhum like registrado.")
                else:
                    for like in likes:
                        print(f"  • {like}")

                print("- Interações do tipo 'comment':")
                comments = usuario.obter_interacoes_por_tipo("comment")
                if not comments:
                    print("  • Nenhum comentário registrado.")
                else:
                    for comment in comments:
                        print(f"  • {comment}")

                print("- Interações do tipo 'share':")
                shares = usuario.obter_interacoes_por_tipo("share")
                if not shares:
                    print("  • Nenhum compartilhamento registrado.")
                else:
                    for share in shares:
                        print(f"  • {share}")

                print("- Interações do tipo 'view_start':")
                views_starts = usuario.obter_interacoes_por_tipo("view_start")
                if not views_starts:
                    print("  • Nenhuma visualização registrada.")
                else:
                    for view_start in views_starts:
                        print(f"  • {view_start}")
                print()

                print("- Conteúdos únicos consumidos:")
                for conteudo in usuario.obter_conteudos_unicos_consumidos():
                    print(f"  • {conteudo}")
                print()

                print("- Tempo total de consumo por plataforma:")
                for plataforma in self.__plataformas_registradas.values():
                    tempo = usuario.calcular_tempo_total_consumo_plataforma(plataforma)
                    print(f"  • {plataforma}: {tempo} segundos")
                print()

                print("- Plataformas mais frequentes - Top 3:")
                for plataforma, valor in usuario.plataformas_mais_frequentes(3):
                    print(f"  • {plataforma}: {valor} vez(es)")
                print()

    def identificar_top_conteudos(self, metrica: str, top_n: int = 5):
        metricas = {
            "tempo_total_consumo": "Tempo Total de Consumo",
            "media_tempo_consumo": "Tempo Médio de Consumo",
        }
        print(f"\n--- Relatório: Top {top_n} Conteúdos por {metricas[metrica]} ---")
        todos_conteudos = self.__arvore_conteudos.percurso_em_ordem()
        if metrica == "tempo_total_consumo":
            chave = lambda c: c.calcular_tempo_total_consumo()
        elif metrica == "media_tempo_consumo":
            chave = lambda c: c.calcular_total_interacoes_engajamento()
        else:
            raise ValueError(
                "Métrica inválida. Use 'tempo_total_consumo' ou 'media_tempo_consumo'."
            )
        ordenados = quick_sort(todos_conteudos, chave=chave)[::-1]
        for i, c in enumerate(ordenados[:top_n]):
            print(f"{i + 1}. '{c.nome_conteudo}' | {metricas[metrica]}: {chave(c)}")
