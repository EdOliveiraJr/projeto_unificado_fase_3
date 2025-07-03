# from analise import Sistema

# def pipeline():
#     print("************ Iniciando pipeline completo ************\n")

#     sistema = Sistema()

#     # 1. Processar CSV
#     print("1. Carregando e processando interações do CSV")
#     sistema.processar_interacoes_do_csv("interacoes_globo.csv")
#     print("-> Interações carregadas e processadas.\n")

#     # 2. Listar plataformas
#     print("2. Listando plataformas registradas")
#     plataformas = sistema.listar_plataformas()
#     for p in plataformas:
#         print(f"- {p}")
#     print('\n ******************************************\n')
    
#     # 3. Relatório de engajamento dos conteúdos
#     print("3. Gerando relatório de engajamento dos conteúdos")
#     sistema.gerar_relatorio_engajamento_conteudos()
#     print('\n ******************************************\n')

#     # 4. Relatório de atividade dos usuários
#     print("4. Gerando relatório de atividade dos usuários")
#     sistema.gerar_relatorio_atividade_usuarios()
#     print('\n ******************************************\n')

#     print("5. Relatório de métricas de conteúdos")
#     print("Métrica - Total total de consumo")
#     sistema.identificar_top_conteudos('tempo_total_consumo')
#     print()
#     print("Métrica - Média de tempo de consumo")
#     sistema.identificar_top_conteudos('media_tempo_consumo')
#     print()


# if __name__ == "__main__":
#              info = '''
#         Projeto Formação em Tecnologia Rede Globo
#         Fase 2: Análise de Engajamento de Mídias Globo com POO
        
#         Turma: 1372
#         Professor: Bruno e Maurício
#         Equipe:
#                 Edvaldo Oliveira
#                 Daniel Brambila
#                 Malu Fazendo
#                 Lucas Sandes
#                 Danilo Pinho
#                 Felipe Martins
#     '''
# print(info)
# pipeline()
# print("************ Pipeline executado com sucesso! ************")


# /main.py


from analise.sistema import SistemaAnaliseEngajamento

def pipeline_fase_3():
    print("************ Iniciando Pipeline - Fase 3 ************\n")
    print("Análise de Engajamento com Estruturas de Dados e Algoritmos\n")

    sistema = SistemaAnaliseEngajamento()

    # 1. Carregar dados do CSV para a Fila
    print("Passo 1: Carregando interações do CSV para a fila de processamento...")
    sistema.carregar_interacoes_para_fila("interacoes_globo.csv")
    print("-> Carga para a fila concluída.\n")

    # 2. Processar interações da Fila para as Árvores
    print("Passo 2: Processando interações da fila e populando as árvores...")
    sistema.processar_interacoes_da_fila()
    print("-> Processamento e população das árvores concluídos.\n")

    # 3. Gerar Relatórios Ordenados
    print("Passo 3: Gerando relatórios de engajamento com ordenação...")
    
    # Relatório de Top 5 conteúdos por tempo total de consumo
    sistema.gerar_relatorio_top_conteudos(metrica='tempo_total_consumo', top_n=5)
    
    # Relatório de Top 5 conteúdos por total de interações de engajamento
    sistema.gerar_relatorio_top_conteudos(metrica='total_interacoes', top_n=5)
    
    print("\n----------------------------------------------------")


if __name__ == "__main__":
    info = '''
    Projeto Formação em Tecnologia Rede Globo
    Fase 3: Análise de Engajamento com Estruturas de Dados
    
    Turma: 1372
    Professor: Jorge Cristhian Chamby
    Equipe:
            Danilo, Daniel, Edvaldo, Malu, Felipe, Lucas
    '''
    print(info)
    pipeline_fase_3()
    print("\n************  executado com sucesso! ************")
