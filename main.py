from analise import Sistema
import sys

def exibir_menu():
    print("\n====== MENU DE ANÁLISE DE ENGAJAMENTO ======")
    print("1. Carregar e processar interações do CSV")
    print("2. Listar plataformas registradas")
    print("3. Gerar relatório de engajamento dos conteúdos")
    print("4. Gerar relatório de atividade dos usuários")
    print("5. Identificar top conteúdos por métrica")
    print("6. Sair")
    print("============================================")

def main():
    sistema = Sistema()
    csv_path = "interacoes_globo.csv"  # ajuste se necessário

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                sistema.processar_interacoes_do_csv(csv_path)
                print("Interações carregadas e processadas com sucesso.")
            except Exception as e:
                print(f"Erro ao processar CSV: {e}")

        elif opcao == "2":
            plataformas = sistema.listar_plataformas()
            if plataformas:
                print("Plataformas registradas:")
                for p in plataformas:
                    print(f"- {p}")
            else:
                print("Nenhuma plataforma registrada.")

        elif opcao == "3":
            try:
                sistema.gerar_relatorio_engajamento_conteudos()
            except Exception as e:
                print(f"Erro ao gerar relatório: {e}")

        elif opcao == "4":
            try:
                sistema.gerar_relatorio_atividade_usuarios()
            except Exception as e:
                print(f"Erro ao gerar relatório: {e}")

        elif opcao == "5":
            print("Escolha a métrica:")
            print("a) tempo_total_consumo")
            print("b) media_tempo_consumo")
            metrica = input("Digite a letra correspondente: ").strip().lower()
            if metrica == "a":
                metrica_nome = "tempo_total_consumo"
            elif metrica == "b":
                metrica_nome = "media_tempo_consumo"
            else:
                print("Opção de métrica inválida.")
                continue
            try:
                sistema.identificar_top_conteudos(metrica_nome)
            except Exception as e:
                print(f"Erro ao identificar top conteúdos: {e}")

        elif opcao == "6":
            print("Saindo do programa...")
            sys.exit(0)

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    info = """
****************************************************************
*                                                              *
*                 Projeto Unificado - Fase 3                   *
*           Análise de Engajamento de Mídias Globo             *
*                  com Estruturas de Dados                     *
*   Módulo Foco: DS-PY-003 (Introdução a Algoritmos e          *
*                 Estruturas de Dados)                         *
*                                                              *
*   Descrição: Aplicar os princípios fundamentais de           *
*   Algoritmos e Estruturas de Dados na análise de dados       *
*   de engajamento de mídias, utilizando as estruturas de      *
*   dados adequadas para otimizar o processamento e a          *
*   recuperação de informações.                                *
*                                                              *
*   Turma: 1372                Professor: Jorge                *
*   Data: 07/07/2025                                           *
*                                                              *
*   Alunos:                                                    *
*     Edvaldo Oliveira                                         *
*     Daniel Brambila                                          *
*     Malu Fazendo                                             *
*     Lucas Sandes                                             *
*     Danilo Pinho                                             *
*     Felipe Martins                                           *
*                                                              *
*                 Equipe: Serpentes Tech                       *
****************************************************************
"""
    print(info)
    main()





