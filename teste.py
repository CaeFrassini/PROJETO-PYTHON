# UNITECH - Sistema de Reforço de Estudo Personalizado
import random

def fazer_quiz_html(quiz_html, biblioteca):
    """Função para realizar o quiz de HTML com 3 tentativas e reforço personalizado"""
    
    tentativas = 0
    max_tentativas = 3
    nota_minima = 70
    
    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\n🎯 QUIZ DE HTML - TENTATIVA {tentativas}/3")
        print("=" * 50)
        
        # Seleciona 2 perguntas aleatórias de cada capítulo (total: 12 perguntas)
        perguntas_quiz = []
        for capitulo in range(1, 7):
            perguntas_capitulo = quiz_html[capitulo].copy()
            random.shuffle(perguntas_capitulo)
            perguntas_quiz.extend(perguntas_capitulo[:2])  # 2 perguntas por capítulo
        
        random.shuffle(perguntas_quiz)
        
        acertos = 0
        respostas_erradas = []
        
        # Aplica o quiz
        for i, pergunta in enumerate(perguntas_quiz, 1):
            print(f"\n📝 PERGUNTA {i}/12:")
            print(pergunta["pergunta"])
            for opcao in pergunta["opcoes"]:
                print(opcao)
            
            resposta_usuario = input("\nSua resposta (A, B, C ou D): ").upper().strip()
            
            if resposta_usuario == pergunta["resposta"]:
                print("✅ Correto!")
                acertos += 1
            else:
                print(f"❌ Incorreto! A resposta correta é: {pergunta['resposta']}")
                respostas_erradas.append(pergunta)
        
        # Calcula a nota
        nota = (acertos / len(perguntas_quiz)) * 100
        print(f"\n📊 RESULTADO DA TENTATIVA {tentativas}:")
        print(f"Acertos: {acertos}/{len(perguntas_quiz)}")
        print(f"Nota: {nota:.1f}%")
        
        if nota >= nota_minima:
            print("🎉 PARABÉNS! VOCÊ FOI APROVADO!")
            print("✅ Quiz concluído com sucesso!")
            return
        else:
            print(f"⚠️ Nota insuficiente. Mínimo necessário: {nota_minima}%")
            
            if tentativas < max_tentativas:
                print(f"\nVocê ainda tem {max_tentativas - tentativas} tentativa(s).")
                
                # Gera reforço personalizado baseado nos erros
                gerar_plano_reforco_personalizado(respostas_erradas, biblioteca)
                
                continuar = input("\nDeseja tentar novamente? (S/N): ").upper().strip()
                if continuar != 'S':
                    break
            else:
                print("\n❌ LIMITE DE TENTATIVAS ATINGIDO!")
                print("📚 PLANO DE REFORÇO FINAL:")
                gerar_plano_reforco_personalizado(respostas_erradas, biblioteca)
                print("\n💡 Recomendação: Estude mais e procure seu mentor para orientação adicional.")

def gerar_plano_reforco_personalizado(respostas_erradas, biblioteca):
    """Gera um plano de reforço personalizado baseado nos erros do aluno"""
    print("\n📋 PLANO DE REFORÇO PERSONALIZADO:")
    print("=" * 40)
    
    # Agrupa erros por capítulo
    erros_por_capitulo = {}
    for erro in respostas_erradas:
        capitulo = erro["capitulo"]
        if capitulo not in erros_por_capitulo:
            erros_por_capitulo[capitulo] = []
        erros_por_capitulo[capitulo].append(erro)
    
    # Recursos de reforço por capítulo - múltiplas opções para randomização
    recursos_reforco = {
        1: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/html",
                "https://www.w3schools.com/html/html_basic.asp",
                "https://html.com/document/",
                "https://www.freecodecamp.org/news/html-basics-for-beginners/",
                "https://htmlreference.io/",
                "https://www.codecademy.com/learn/learn-html"
            ],
            "videos": [
                "Pesquise: 'HTML5 estrutura básica' no YouTube",
                "Pesquise: 'HTML document structure tutorial' no YouTube", 
                "Pesquise: 'HTML básico para iniciantes' no YouTube",
                "Pesquise: 'DOCTYPE HTML5 explicação' no YouTube",
                "Pesquise: 'HTML head e body diferenças' no YouTube"
            ],
            "praticas": [
                "Crie 3 páginas HTML básicas com estrutura completa",
                "Desenvolva um site pessoal simples com 5 páginas",
                "Faça uma página 'Sobre Mim' com estrutura HTML5",
                "Crie uma landing page básica para um produto fictício",
                "Desenvolva um portfólio online simples"
            ]
        },
        2: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/header",
                "https://www.w3schools.com/html/html5_semantic_elements.asp",
                "https://html5doctor.com/",
                "https://www.smashingmagazine.com/2013/01/the-importance-of-sections/",
                "https://webdesign.tutsplus.com/articles/quick-tip-use-semantic-html5-elements--webdesign-3384",
                "https://css-tricks.com/why-how-and-when-to-use-semantic-html-and-aria/"
            ],
            "videos": [
                "Pesquise: 'HTML5 semantic elements' no YouTube",
                "Pesquise: 'HTML semântico tutorial completo' no YouTube",
                "Pesquise: 'header nav main aside footer HTML5' no YouTube",
                "Pesquise: 'semantic HTML accessibility' no YouTube",
                "Pesquise: 'HTML5 layout estrutural' no YouTube"
            ],
            "praticas": [
                "Crie uma página usando todas as tags semânticas",
                "Desenvolva um blog layout com header, nav, main, aside e footer",
                "Faça uma página de notícias com estrutura semântica completa",
                "Crie um site de empresa com seções bem definidas",
                "Desenvolva uma página de e-commerce com layout semântico"
            ]
        },
        3: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/form",
                "https://www.w3schools.com/html/html_forms.asp",
                "https://html.com/forms/",
                "https://webdesign.tutsplus.com/articles/bring-your-forms-up-to-date-with-css3-and-html5-validation--webdesign-4738",
                "https://css-tricks.com/form-validation-ux-html-css/",
                "https://www.smashingmagazine.com/2018/08/ux-html5-mobile-form-part-1/"
            ],
            "videos": [
                "Pesquise: 'HTML forms tutorial' no YouTube",
                "Pesquise: 'formulários HTML completo' no YouTube",
                "Pesquise: 'HTML form validation' no YouTube",
                "Pesquise: 'input types HTML5' no YouTube",
                "Pesquise: 'formulário de contato HTML' no YouTube"
            ],
            "praticas": [
                "Crie 3 formulários diferentes (contato, cadastro, pesquisa)",
                "Desenvolva um formulário de inscrição completo com validação",
                "Faça um formulário de feedback com diferentes tipos de input",
                "Crie um formulário de pedido online para restaurante",
                "Desenvolva um formulário de cadastro de usuário com múltiplas etapas"
            ]
        },
        4: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/ul",
                "https://www.w3schools.com/html/html_lists.asp",
                "https://css-tricks.com/almanac/elements/u/ul/",
                "https://html.com/lists/",
                "https://www.codecademy.com/resources/docs/html/lists",
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/a"
            ],
            "videos": [
                "Pesquise: 'HTML lists and links' no YouTube",
                "Pesquise: 'listas HTML ul ol dl' no YouTube",
                "Pesquise: 'HTML navigation menu' no YouTube",
                "Pesquise: 'links HTML target blank' no YouTube",
                "Pesquise: 'menu responsivo HTML' no YouTube"
            ],
            "praticas": [
                "Crie um menu de navegação com listas e links",
                "Desenvolva uma página com diferentes tipos de listas",
                "Faça um menu dropdown usando apenas HTML",
                "Crie uma lista de produtos com links para detalhes",
                "Desenvolva um índice de conteúdo com links internos"
            ]
        },
        5: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/img",
                "https://www.w3schools.com/html/html_media.asp",
                "https://html.com/media/",
                "https://css-tricks.com/almanac/elements/i/img/",
                "https://web.dev/fast/#optimize-your-images",
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/video"
            ],
            "videos": [
                "Pesquise: 'HTML multimedia elements' no YouTube",
                "Pesquise: 'HTML img alt attribute' no YouTube",
                "Pesquise: 'HTML5 video audio tutorial' no YouTube",
                "Pesquise: 'responsive images HTML' no YouTube",
                "Pesquise: 'HTML figure figcaption' no YouTube"
            ],
            "praticas": [
                "Crie uma galeria com imagens, áudio e vídeo",
                "Desenvolva uma página de portfólio com imagens responsivas",
                "Faça um player de música simples com HTML5",
                "Crie uma galeria de fotos com legendas",
                "Desenvolva uma página de apresentação com vídeos incorporados"
            ]
        },
        6: {
            "sites": [
                "https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/table",
                "https://www.w3schools.com/html/html_tables.asp",
                "https://css-tricks.com/complete-guide-table-element/",
                "https://html.com/tables/",
                "https://www.codecademy.com/resources/docs/html/tables",
                "https://webaim.org/techniques/tables/"
            ],
            "videos": [
                "Pesquise: 'HTML tables tutorial' no YouTube",
                "Pesquise: 'tabelas HTML thead tbody tfoot' no YouTube",
                "Pesquise: 'HTML table accessibility' no YouTube",
                "Pesquise: 'responsive HTML tables' no YouTube",
                "Pesquise: 'HTML table styling' no YouTube"
            ],
            "praticas": [
                "Crie 3 tabelas: simples, com cabeçalho e complexa",
                "Desenvolva uma tabela de preços para um serviço",
                "Faça uma tabela de horários de aulas",
                "Crie uma tabela comparativa de produtos",
                "Desenvolva uma tabela de dados financeiros com totais"
            ]
        }
    }
    
    import random
    
    for capitulo in sorted(erros_por_capitulo.keys()):
        titulo_capitulo = biblioteca[capitulo][0]
        num_erros = len(erros_por_capitulo[capitulo])
        
        print(f"\n📖 {titulo_capitulo}")
        print(f"   Erros encontrados: {num_erros}")
        print("   📚 Recursos recomendados:")
        
        recursos = recursos_reforco[capitulo]
        
        # Seleciona 2-3 sites aleatórios
        sites_selecionados = random.sample(recursos["sites"], min(3, len(recursos["sites"])))
        print("   🌐 Sites para estudar:")
        for site in sites_selecionados:
            print(f"     • {site}")
        
        # Seleciona 2-3 vídeos aleatórios
        videos_selecionados = random.sample(recursos["videos"], min(3, len(recursos["videos"])))
        print("   🎥 Vídeos:")
        for video in videos_selecionados:
            print(f"     • {video}")
        
        # Seleciona 1-2 práticas aleatórias
        praticas_selecionadas = random.sample(recursos["praticas"], min(2, len(recursos["praticas"])))
        print("   ✏️ Práticas recomendadas:")
        for pratica in praticas_selecionadas:
            print(f"     • {pratica}")
        
        # Tempo varia baseado no número de erros
        tempo_base = 2 + (num_erros * 0.5)
        tempo_sugerido = f"{tempo_base:.1f}-{tempo_base + 1:.1f} horas"
        print(f"   ⏰ Tempo sugerido: {tempo_sugerido} de estudo")
    
    if erros_por_capitulo:
        print(f"\n💡 DICA GERAL: Revise os capítulos onde você errou mais e pratique os exercícios sugeridos.")
        print("🔄 Após estudar, você pode refazer o quiz para testar seu conhecimento!")

def estudar_capitulos(biblioteca, curso, quiz_html=None):
    """Função para estudar capítulos com navegação avançada"""
    capitulo_atual = 1
    max_capitulos = len(biblioteca)
    
    while True:
        print("\n" + "="*60)
        print("📚 MODO ESTUDO - NAVEGAÇÃO INTERATIVA")
        print("="*60)
        
        print(f"\n📖 CAPÍTULOS DISPONÍVEIS ({curso}):")
        for num, (titulo, _) in biblioteca.items():
            status = "📍 ATUAL" if num == capitulo_atual else "✅ CONCLUÍDO" if num < capitulo_atual else "⏳ PENDENTE"
            print(f"[{num}] {titulo} - {status}")
        
        print(f"\n🎯 OPÇÕES DE NAVEGAÇÃO:")
        print("[1] Estudar capítulo atual")
        print("[2] Escolher capítulo específico")
        print("[3] Ir para próximo capítulo")
        print("[4] Ir para capítulo anterior")
        print("[5] Fazer questionário")
        print("[6] Voltar ao menu principal")
        
        try:
            opcao = int(input(f"\nDigite sua opção (1-6): "))
            
            if opcao == 1:
                # Estudar capítulo atual
                if capitulo_atual <= max_capitulos:
                    titulo, conteudo = biblioteca[capitulo_atual]
                    print(f"\n📚 {titulo}")
                    print("="*50)
                    print(f"📖 Conteúdo:\n{conteudo}\n")
                    print("✅ Estudo concluído!")
                    
                    # Menu pós-estudo
                    while True:
                        print(f"\n🎯 O QUE DESEJA FAZER AGORA?")
                        print("[1] Continuar para o próximo capítulo")
                        print("[2] Fazer questionário")
                        print("[3] Rever este capítulo")
                        print("[4] Escolher outro capítulo")
                        print("[5] Voltar ao menu de navegação")
                        
                        try:
                            acao = int(input("Digite sua opção (1-5): "))
                            
                            if acao == 1:
                                if capitulo_atual < max_capitulos:
                                    capitulo_atual += 1
                                    print(f"➡️ Avançando para o Capítulo {capitulo_atual}")
                                else:
                                    print("🎉 Você completou todos os capítulos!")
                                    print("💡 Que tal fazer o questionário para testar seus conhecimentos?")
                                break
                            elif acao == 2:
                                if curso == "HTML":
                                    fazer_quiz_html(quiz_html, biblioteca)
                                elif curso == "CSS":
                                    fazer_quiz_css(quiz_css, biblioteca)
                                elif curso == "LÓGICA DE PROGRAMAÇÃO":
                                    fazer_quiz_logica(quiz_logica, biblioteca)
                                else:
                                    print("Questionário não disponível para este curso.")
                                break
                            elif acao == 3:
                                print("🔄 Revisando o capítulo atual...")
                                continue
                            elif acao == 4:
                                break
                            elif acao == 5:
                                break
                            else:
                                print("❌ Opção inválida. Tente novamente.")
                        except ValueError:
                            print("❌ Digite apenas números de 1 a 5.")
                else:
                    print("🎉 Você já completou todos os capítulos!")
            
            elif opcao == 2:
                # Escolher capítulo específico
                print("\n📚 ESCOLHA UM CAPÍTULO:")
                for num, (titulo, _) in biblioteca.items():
                    print(f"[{num}] {titulo}")
                
                try:
                    cap_escolhido = int(input("Digite o número do capítulo: "))
                    if cap_escolhido in biblioteca:
                        capitulo_atual = cap_escolhido
                        print(f"📍 Capítulo {capitulo_atual} selecionado!")
                    else:
                        print("❌ Capítulo inválido.")
                except ValueError:
                    print("❌ Digite um número válido.")
            
            elif opcao == 3:
                # Próximo capítulo
                if capitulo_atual < max_capitulos:
                    capitulo_atual += 1
                    print(f"➡️ Avançando para o Capítulo {capitulo_atual}")
                else:
                    print("❌ Você já está no último capítulo!")
            
            elif opcao == 4:
                # Capítulo anterior
                if capitulo_atual > 1:
                    capitulo_atual -= 1
                    print(f"⬅️ Voltando para o Capítulo {capitulo_atual}")
                else:
                    print("❌ Você já está no primeiro capítulo!")
            
            elif opcao == 5:
                # Fazer questionário baseado no curso atual
                if curso == "HTML":
                    fazer_quiz_html(quiz_html, biblioteca)
                elif curso == "CSS":
                    fazer_quiz_css(quiz_css, biblioteca)
                elif curso == "LÓGICA DE PROGRAMAÇÃO":
                    fazer_quiz_logica(quiz_logica, biblioteca)
                else:
                    print("❌ c não disponível para este curso.")
            
            elif opcao == 6:
                # Voltar ao menu principal
                print("🔙 Voltando ao menu principal...")
                break
            
            else:
                print("❌ Opção inválida. Digite um número de 1 a 6.")
                
        except ValueError:
            print("❌ Digite apenas números de 1 a 6.")

# Quiz CSS - Expandido com mais perguntas
quiz_css = {
    1: [
        ("Qual é a forma correta de aplicar CSS externo?", ["<link rel='stylesheet' href='estilo.css'>", "<style src='estilo.css'>", "<css href='estilo.css'>", "<import css='estilo.css'>"], 0),
        ("Como selecionar um elemento por classe?", [".classe", "#classe", "classe", "*classe"], 0),
        ("Qual seletor tem maior especificidade?", ["elemento", ".classe", "#id", "*"], 2),
        ("Como aplicar CSS apenas para telas menores que 768px?", ["@media (max-width: 768px)", "@screen (max: 768px)", "@responsive (768px)", "@mobile (768px)"], 0),
        ("Qual propriedade define a cor do texto?", ["text-color", "font-color", "color", "foreground"], 2),
        ("Como importar uma fonte do Google Fonts no CSS?", ["@import url('fonts.google.com')", "@font-face", "@import url('fonts.googleapis.com')", "font-import"], 2)
    ],
    2: [
        ("Qual propriedade define o espaçamento interno?", ["margin", "padding", "border", "spacing"], 1),
        ("Como centralizar um elemento horizontalmente?", ["margin: 0 auto", "text-align: center", "center: true", "align: center"], 0),
        ("Qual é a ordem correta do Box Model (de dentro para fora)?", ["content → padding → border → margin", "margin → border → padding → content", "padding → content → border → margin", "content → border → padding → margin"], 0),
        ("Como fazer um elemento ocupar toda a largura disponível?", ["width: 100%", "width: full", "width: auto", "width: max"], 0),
        ("Qual valor de display faz o elemento desaparecer?", ["hidden", "invisible", "none", "transparent"], 2),
        ("Como definir uma altura mínima de 300px?", ["height: 300px min", "min-height: 300px", "height-min: 300px", "minimum-height: 300px"], 1),
        ("Qual propriedade controla o espaçamento entre linhas?", ["line-spacing", "text-spacing", "line-height", "row-height"], 2),
        ("Como fazer bordas arredondadas?", ["border-curve", "border-radius", "border-round", "corner-radius"], 1)
    ],
    3: [
        ("Qual propriedade cria um container flexível?", ["display: flex", "flex: true", "layout: flex", "flexbox: on"], 0),
        ("Como distribuir espaço igualmente entre itens flex?", ["justify-content: space-between", "align-items: center", "flex-wrap: wrap", "gap: 10px"], 0),
        ("Qual propriedade alinha itens no eixo cruzado do Flexbox?", ["justify-content", "align-items", "flex-align", "cross-align"], 1),
        ("Como fazer um item flex crescer para ocupar espaço disponível?", ["flex-grow: 1", "flex-expand: 1", "grow: 1", "expand: true"], 0),
        ("Qual propriedade permite quebra de linha em containers flex?", ["flex-wrap: wrap", "flex-break: wrap", "wrap: true", "line-break: flex"], 0),
        ("Como criar um grid com 3 colunas iguais?", ["grid-template-columns: 1fr 1fr 1fr", "grid-columns: 3", "columns: 3 equal", "grid: 3-columns"], 0),
        ("Qual propriedade define o espaçamento entre itens do grid?", ["grid-spacing", "gap", "grid-margin", "item-spacing"], 1),
        ("Como fazer um item ocupar 2 colunas no grid?", ["grid-column: span 2", "column-span: 2", "grid-width: 2", "columns: 2"], 0),
        ("Qual valor de justify-content centraliza itens horizontalmente?", ["center", "middle", "centered", "horizontal-center"], 0),
        ("Como criar um layout responsivo com Grid?", ["Usar fr e minmax()", "Usar apenas px", "Usar apenas %", "Usar apenas em"], 0)
    ]
}

# Quiz Lógica de Programação
quiz_logica = {
    1: [
        ("Qual é a sequência correta para resolver um problema?", ["Algoritmo → Código → Teste", "Código → Algoritmo → Teste", "Teste → Código → Algoritmo", "Algoritmo → Teste → Código"], 0),
        ("Qual tipo de dado representa True/False?", ["Boolean", "String", "Integer", "Float"], 0)
    ],
    2: [
        ("Qual estrutura executa código apenas se uma condição for verdadeira?", ["if", "for", "while", "def"], 0),
        ("Como criar um loop que executa 5 vezes?", ["for i in range(5)", "while i < 5", "if i == 5", "loop 5 times"], 0)
    ],
    3: [
        ("Como adicionar um item ao final de uma lista?", ["lista.append(item)", "lista.add(item)", "lista.insert(item)", "lista.push(item)"], 0),
        ("Qual palavra-chave define uma função?", ["def", "function", "func", "define"], 0)
    ]
}

def fazer_quiz_css(quiz_css, biblioteca):
    tentativas = 0
    max_tentativas = 3
    nota_minima = 70
    
    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\n🎯 AVALIAÇÃO CSS - TENTATIVA {tentativas}/{max_tentativas}")
        print("=" * 50)
        
        # Selecionar 2 perguntas de cada capítulo (6 perguntas total)
        perguntas_selecionadas = []
        capitulos_com_erro = []
        
        for capitulo in range(1, 4):  # 3 capítulos
            perguntas_capitulo = quiz_css[capitulo].copy()
            random.shuffle(perguntas_capitulo)
            perguntas_selecionadas.extend(perguntas_capitulo[:2])
        
        random.shuffle(perguntas_selecionadas)
        
        acertos = 0
        total_perguntas = len(perguntas_selecionadas)
        
        for i, (pergunta, opcoes, resposta_correta) in enumerate(perguntas_selecionadas, 1):
            print(f"\n📝 PERGUNTA {i}:")
            print(pergunta)
            
            for j, opcao in enumerate(opcoes):
                print(f"{j + 1}. {opcao}")
            
            try:
                resposta_usuario = int(input("Sua resposta (1-4): ")) - 1
                
                if resposta_usuario == resposta_correta:
                    print("✅ CORRETO!")
                    acertos += 1
                else:
                    print(f"❌ INCORRETO! A resposta correta é: {opcoes[resposta_correta]}")
                    # Identificar capítulo com erro
                    for cap in range(1, 4):
                        if (pergunta, opcoes, resposta_correta) in quiz_css[cap]:
                            if cap not in capitulos_com_erro:
                                capitulos_com_erro.append(cap)
                            break
                            
            except (ValueError, IndexError):
                print("❌ RESPOSTA INVÁLIDA! Considerando como erro.")
                for cap in range(1, 4):
                    if (pergunta, opcoes, resposta_correta) in quiz_css[cap]:
                        if cap not in capitulos_com_erro:
                            capitulos_com_erro.append(cap)
                        break
        
        # Calcular nota
        nota = (acertos / total_perguntas) * 100
        print(f"\n📊 RESULTADO:")
        print(f"Acertos: {acertos}/{total_perguntas}")
        print(f"Nota: {nota:.1f}%")
        
        if nota >= nota_minima:
            print("🎉 PARABÉNS! VOCÊ FOI APROVADO!")
            break
        else:
            print(f"📚 Você precisa de pelo menos {nota_minima}% para ser aprovado.")
            
            if tentativas < max_tentativas:
                print("\n🎯 PLANO DE REFORÇO PERSONALIZADO:")
                
                recursos_css = {
                    1: {
                        "sites": [
                            "https://developer.mozilla.org/pt-BR/docs/Web/CSS",
                            "https://www.w3schools.com/css/css_intro.asp",
                            "https://css-tricks.com/almanac/",
                            "https://cssreference.io/",
                            "https://www.freecodecamp.org/news/css-selectors-cheat-sheet/",
                            "https://specificity.keegan.st/",
                            "https://flukeout.github.io/",
                            "https://www.codecademy.com/learn/learn-css"
                        ],
                        "videos": [
                            "Pesquise: 'CSS básico para iniciantes' no YouTube",
                            "Pesquise: 'CSS seletores tutorial completo' no YouTube",
                            "Pesquise: 'CSS especificidade explicada' no YouTube",
                            "Pesquise: 'CSS externo interno inline diferenças' no YouTube",
                            "Pesquise: 'CSS cores e fontes tutorial' no YouTube",
                            "Pesquise: 'CSS media queries responsivo' no YouTube"
                        ],
                        "praticas": [
                            "Crie uma página com CSS externo aplicando diferentes seletores",
                            "Desenvolva um sistema de cores consistente para um site",
                            "Faça uma página responsiva usando media queries",
                            "Crie um menu de navegação estilizado com CSS",
                            "Desenvolva uma galeria de imagens com hover effects"
                        ]
                    },
                    2: {
                        "sites": [
                            "https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Box_Model",
                            "https://www.w3schools.com/css/css_boxmodel.asp",
                            "https://css-tricks.com/the-css-box-model/",
                            "https://internetingishard.com/html-and-css/css-box-model/",
                            "https://www.codecademy.com/resources/docs/css/box-model",
                            "https://boxmodel.com/",
                            "https://web.dev/learn/css/box-model/",
                            "https://cssreference.io/box-model/"
                        ],
                        "videos": [
                            "Pesquise: 'CSS Box Model explicado detalhadamente' no YouTube",
                            "Pesquise: 'CSS margin padding border diferenças' no YouTube",
                            "Pesquise: 'CSS centralizar elementos tutorial' no YouTube",
                            "Pesquise: 'CSS display block inline inline-block' no YouTube",
                            "Pesquise: 'CSS position absolute relative fixed' no YouTube",
                            "Pesquise: 'CSS width height min-max tutorial' no YouTube"
                        ],
                        "praticas": [
                            "Crie cards com diferentes espaçamentos usando box model",
                            "Desenvolva um layout com elementos centralizados",
                            "Faça uma página com diferentes tipos de display",
                            "Crie um sistema de grid simples usando float",
                            "Desenvolva uma sidebar fixa com position"
                        ]
                    },
                    3: {
                        "sites": [
                            "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
                            "https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Flexible_Box_Layout",
                            "https://flexboxfroggy.com/",
                            "https://css-tricks.com/snippets/css/complete-guide-grid/",
                            "https://cssgridgarden.com/",
                            "https://gridbyexample.com/",
                            "https://www.w3schools.com/css/css3_flexbox.asp",
                            "https://flexbox.malven.co/"
                        ],
                        "videos": [
                            "Pesquise: 'CSS Flexbox tutorial completo' no YouTube",
                            "Pesquise: 'CSS Grid layout do zero' no YouTube",
                            "Pesquise: 'Flexbox vs Grid quando usar' no YouTube",
                            "Pesquise: 'CSS Flexbox justify-content align-items' no YouTube",
                            "Pesquise: 'CSS Grid template areas tutorial' no YouTube",
                            "Pesquise: 'Layout responsivo com Flexbox e Grid' no YouTube"
                        ],
                        "praticas": [
                            "Crie uma navbar responsiva com Flexbox",
                            "Desenvolva um layout de página completo com CSS Grid",
                            "Faça uma galeria de fotos usando Flexbox",
                            "Crie um dashboard com Grid template areas",
                            "Desenvolva um sistema de cards responsivo com Flexbox"
                        ]
                    }
                }
                
                plano_reforco = []
                tempo_estudo = len(capitulos_com_erro) * 30
                
                for capitulo in capitulos_com_erro:
                    recursos_cap = recursos_css[capitulo]
                    
                    # Seleciona 2-3 sites aleatórios
                    sites_selecionados = random.sample(recursos_cap["sites"], min(3, len(recursos_cap["sites"])))
                    plano_reforco.append("🌐 Sites para estudar:")
                    for site in sites_selecionados:
                        plano_reforco.append(f"   • {site}")
                    
                    # Seleciona 2-3 vídeos aleatórios
                    videos_selecionados = random.sample(recursos_cap["videos"], min(3, len(recursos_cap["videos"])))
                    plano_reforco.append("🎥 Vídeos:")
                    for video in videos_selecionados:
                        plano_reforco.append(f"   • {video}")
                    
                    # Seleciona 1-2 práticas aleatórias
                    praticas_selecionadas = random.sample(recursos_cap["praticas"], min(2, len(recursos_cap["praticas"])))
                    plano_reforco.append("✏️ Práticas recomendadas:")
                    for pratica in praticas_selecionadas:
                        plano_reforco.append(f"   • {pratica}")
                
                random.shuffle(plano_reforco)
                
                print(f"⏰ Tempo de estudo recomendado: {tempo_estudo} minutos")
                print("📋 Recursos recomendados:")
                for item in plano_reforco:
                    print(f"   {item}")
                
                print(f"\n🔄 Você ainda tem {max_tentativas - tentativas} tentativa(s).")
                continuar = input("Deseja tentar novamente após estudar? (s/n): ").lower()
                if continuar != 's':
                    break
            else:
                print("❌ VOCÊ ESGOTOU SUAS TENTATIVAS. PROCURE SEU MENTOR PARA ORIENTAÇÃO.")

def fazer_quiz_logica(quiz_logica, biblioteca):
    tentativas = 0
    max_tentativas = 3
    nota_minima = 70
    
    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\n🎯 AVALIAÇÃO LÓGICA DE PROGRAMAÇÃO - TENTATIVA {tentativas}/{max_tentativas}")
        print("=" * 60)
        
        # Selecionar 2 perguntas de cada capítulo (6 perguntas total)
        perguntas_selecionadas = []
        capitulos_com_erro = []
        
        for capitulo in range(1, 4):  # 3 capítulos
            perguntas_capitulo = quiz_logica[capitulo].copy()
            random.shuffle(perguntas_capitulo)
            perguntas_selecionadas.extend(perguntas_capitulo[:2])
        
        random.shuffle(perguntas_selecionadas)
        
        acertos = 0
        total_perguntas = len(perguntas_selecionadas)
        
        for i, (pergunta, opcoes, resposta_correta) in enumerate(perguntas_selecionadas, 1):
            print(f"\n📝 PERGUNTA {i}:")
            print(pergunta)
            
            for j, opcao in enumerate(opcoes):
                print(f"{j + 1}. {opcao}")
            
            try:
                resposta_usuario = int(input("Sua resposta (1-4): ")) - 1
                
                if resposta_usuario == resposta_correta:
                    print("✅ CORRETO!")
                    acertos += 1
                else:
                    print(f"❌ INCORRETO! A resposta correta é: {opcoes[resposta_correta]}")
                    # Identificar capítulo com erro
                    for cap in range(1, 4):
                        if (pergunta, opcoes, resposta_correta) in quiz_logica[cap]:
                            if cap not in capitulos_com_erro:
                                capitulos_com_erro.append(cap)
                            break
                            
            except (ValueError, IndexError):
                print("❌ RESPOSTA INVÁLIDA! Considerando como erro.")
                for cap in range(1, 4):
                    if (pergunta, opcoes, resposta_correta) in quiz_logica[cap]:
                        if cap not in capitulos_com_erro:
                            capitulos_com_erro.append(cap)
                        break
        
        # Calcular nota
        nota = (acertos / total_perguntas) * 100
        print(f"\n📊 RESULTADO:")
        print(f"Acertos: {acertos}/{total_perguntas}")
        print(f"Nota: {nota:.1f}%")
        
        if nota >= nota_minima:
            print("🎉 PARABÉNS! VOCÊ FOI APROVADO!")
            break
        else:
            print(f"📚 Você precisa de pelo menos {nota_minima}% para ser aprovado.")
            
            if tentativas < max_tentativas:
                print("\n🎯 PLANO DE REFORÇO PERSONALIZADO:")
                
                recursos_logica = {
                    1: {
                        "sites": [
                            "https://www.codecademy.com/learn/learn-python-3",
                            "https://www.w3schools.com/python/python_intro.asp",
                            "https://docs.python.org/pt-br/3/tutorial/",
                            "https://penseallen.github.io/PensePython2e/",
                            "https://python.org.br/introducao/",
                            "https://www.freecodecamp.org/learn/scientific-computing-with-python/",
                            "https://algoritmosempython.com.br/",
                            "https://www.programiz.com/python-programming"
                        ],
                        "videos": [
                            "Pesquise: 'Lógica de programação para iniciantes' no YouTube",
                            "Pesquise: 'Algoritmos e fluxogramas tutorial' no YouTube",
                            "Pesquise: 'Variáveis e tipos de dados Python' no YouTube",
                            "Pesquise: 'Operadores aritméticos relacionais lógicos' no YouTube",
                            "Pesquise: 'Como pensar como programador' no YouTube",
                            "Pesquise: 'Pseudocódigo e algoritmos básicos' no YouTube"
                        ],
                        "praticas": [
                            "Crie algoritmos simples no papel antes de programar",
                            "Desenvolva uma calculadora básica com 4 operações",
                            "Faça um programa que converte temperaturas",
                            "Crie um algoritmo para calcular média de notas",
                            "Desenvolva um programa que determina se um número é par ou ímpar"
                        ]
                    },
                    2: {
                        "sites": [
                            "https://docs.python.org/pt-br/3/tutorial/controlflow.html",
                            "https://www.w3schools.com/python/python_conditions.asp",
                            "https://www.programiz.com/python-programming/if-elif-else",
                            "https://realpython.com/python-conditional-statements/",
                            "https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-control-flow",
                            "https://penseallen.github.io/PensePython2e/05-cond-recur.html",
                            "https://python.org.br/introducao/#estruturas-de-controle",
                            "https://www.tutorialspoint.com/python/python_loops.htm"
                        ],
                        "videos": [
                            "Pesquise: 'Python if else elif tutorial completo' no YouTube",
                            "Pesquise: 'Python for while loops explicados' no YouTube",
                            "Pesquise: 'Estruturas condicionais Python exemplos' no YouTube",
                            "Pesquise: 'Python break continue pass comandos' no YouTube",
                            "Pesquise: 'Laços de repetição Python prática' no YouTube",
                            "Pesquise: 'Python range função tutorial' no YouTube"
                        ],
                        "praticas": [
                            "Crie um sistema de notas com múltiplas condições",
                            "Desenvolva um programa de menu com while loop",
                            "Faça um jogo de adivinhação de números",
                            "Crie uma tabuada usando for loop",
                            "Desenvolva um validador de senha com condições"
                        ]
                    },
                    3: {
                        "sites": [
                            "https://docs.python.org/pt-br/3/tutorial/datastructures.html",
                            "https://www.w3schools.com/python/python_lists.asp",
                            "https://realpython.com/python-lists-tuples/",
                            "https://www.programiz.com/python-programming/list",
                            "https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions",
                            "https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-functions",
                            "https://penseallen.github.io/PensePython2e/03-funcoes.html",
                            "https://python.org.br/introducao/#estruturas-de-dados"
                        ],
                        "videos": [
                            "Pesquise: 'Python listas tutorial completo' no YouTube",
                            "Pesquise: 'Python dicionários explicados' no YouTube",
                            "Pesquise: 'Python funções def return' no YouTube",
                            "Pesquise: 'Python estruturas de dados práticas' no YouTube",
                            "Pesquise: 'Python métodos de lista append remove' no YouTube",
                            "Pesquise: 'Python parâmetros argumentos funções' no YouTube"
                        ],
                        "praticas": [
                            "Crie um sistema de cadastro completo com listas",
                            "Desenvolva funções que manipulam listas e dicionários",
                            "Faça um programa de agenda de contatos",
                            "Crie um sistema de estoque com funções",
                            "Desenvolva um jogo da forca usando listas"
                        ]
                    }
                }
                
                plano_reforco = []
                tempo_estudo = len(capitulos_com_erro) * 45
                
                for capitulo in capitulos_com_erro:
                    recursos_cap = recursos_logica[capitulo]
                    
                    # Seleciona 2-3 sites aleatórios
                    sites_selecionados = random.sample(recursos_cap["sites"], min(3, len(recursos_cap["sites"])))
                    plano_reforco.append("🌐 Sites para estudar:")
                    for site in sites_selecionados:
                        plano_reforco.append(f"   • {site}")
                    
                    # Seleciona 2-3 vídeos aleatórios
                    videos_selecionados = random.sample(recursos_cap["videos"], min(3, len(recursos_cap["videos"])))
                    plano_reforco.append("🎥 Vídeos:")
                    for video in videos_selecionados:
                        plano_reforco.append(f"   • {video}")
                    
                    # Seleciona 1-2 práticas aleatórias
                    praticas_selecionadas = random.sample(recursos_cap["praticas"], min(2, len(recursos_cap["praticas"])))
                    plano_reforco.append("✏️ Práticas recomendadas:")
                    for pratica in praticas_selecionadas:
                        plano_reforco.append(f"   • {pratica}")
                
                random.shuffle(plano_reforco)
                
                print(f"⏰ Tempo de estudo recomendado: {tempo_estudo} minutos")
                print("📋 Recursos recomendados:")
                for item in plano_reforco:
                    print(f"   {item}")
                
                print(f"\n🔄 Você ainda tem {max_tentativas - tentativas} tentativa(s).")
                continuar = input("Deseja tentar novamente após estudar? (s/n): ").lower()
                if continuar != 's':
                    break
            else:
                print("❌ VOCÊ ESGOTOU SUAS TENTATIVAS. PROCURE SEU MENTOR PARA ORIENTAÇÃO.")

def unitech():
    print("BEM-VINDO AO UNITECH\n")

    while True:  # Loop principal para permitir mudança de curso
        # Lista de cursos
        cursos = ["HTML", "CSS", "LÓGICA DE PROGRAMAÇÃO"]

        print("CURSOS DISPONÍVEIS:")
        for i, curso in enumerate(cursos, start=1):
            print(f"{i} - {curso}")
        
        try:
            opcao = int(input("SELECIONE O NÚMERO DO CURSO: "))
            if 1 <= opcao <= len(cursos):
                curso = cursos[opcao - 1]
                print(f"\nVOCÊ ESCOLHEU: {curso}\n")
                break
            else:
                print("❌ Opção inválida. Escolha um número de 1 a 3.")
        except ValueError:
            print("❌ Digite apenas números de 1 a 3.")

    # Capítulos e conteúdos de cada curso
    biblioteca = {}
    
    # Quiz de HTML - Perguntas por capítulo
    quiz_html = {
        1: [
            {"pergunta": "Qual tag declara que o documento é HTML5?", 
             "opcoes": ["A) <html5>", "B) <!DOCTYPE html>", "C) <doctype>", "D) <version>"], 
             "resposta": "B", "capitulo": 1},
            {"pergunta": "Onde ficam os metadados de uma página HTML?", 
             "opcoes": ["A) <body>", "B) <footer>", "C) <head>", "D) <meta>"], 
             "resposta": "C", "capitulo": 1},
            {"pergunta": "Qual atributo define o idioma do documento?", 
             "opcoes": ["A) language", "B) lang", "C) idioma", "D) locale"], 
             "resposta": "B", "capitulo": 1}
        ],
        2: [
            {"pergunta": "Qual tag representa o cabeçalho de uma página?", 
             "opcoes": ["A) <head>", "B) <header>", "C) <top>", "D) <title>"], 
             "resposta": "B", "capitulo": 2},
            {"pergunta": "A tag <main> deve aparecer quantas vezes por documento?", 
             "opcoes": ["A) Várias vezes", "B) Duas vezes", "C) Uma vez", "D) Nenhuma"], 
             "resposta": "C", "capitulo": 2},
            {"pergunta": "Qual tag é usada para conteúdo complementar?", 
             "opcoes": ["A) <side>", "B) <aside>", "C) <extra>", "D) <complement>"], 
             "resposta": "B", "capitulo": 2}
        ],
        3: [
            {"pergunta": "Qual tag cria um campo de texto em formulários?", 
             "opcoes": ["A) <text>", "B) <field>", "C) <input>", "D) <textbox>"], 
             "resposta": "C", "capitulo": 3},
            {"pergunta": "Qual atributo define o tipo de um input?", 
             "opcoes": ["A) kind", "B) type", "C) format", "D) style"], 
             "resposta": "B", "capitulo": 3}
        ],
        4: [
            {"pergunta": "Qual tag cria uma lista não ordenada?", 
             "opcoes": ["A) <ol>", "B) <list>", "C) <ul>", "D) <unordered>"], 
             "resposta": "C", "capitulo": 4},
            {"pergunta": "Qual atributo do link abre em nova aba?", 
             "opcoes": ["A) new='true'", "B) target='_blank'", "C) open='new'", "D) window='new'"], 
             "resposta": "B", "capitulo": 4},
            {"pergunta": "Qual tag define um item de lista?", 
             "opcoes": ["A) <item>", "B) <li>", "C) <list-item>", "D) <element>"], 
             "resposta": "B", "capitulo": 4}
        ],
        5: [
            {"pergunta": "Qual atributo é obrigatório na tag <img>?", 
             "opcoes": ["A) width", "B) height", "C) alt", "D) title"], 
             "resposta": "C", "capitulo": 5},
            {"pergunta": "Qual tag adiciona legenda a uma imagem?", 
             "opcoes": ["A) <caption>", "B) <figcaption>", "C) <legend>", "D) <label>"], 
             "resposta": "B", "capitulo": 5},
            {"pergunta": "Qual tag reproduz áudio na página?", 
             "opcoes": ["A) <sound>", "B) <music>", "C) <audio>", "D) <media>"], 
             "resposta": "C", "capitulo": 5}
        ],
        6: [
            {"pergunta": "Qual tag cria uma célula de cabeçalho em tabelas?", 
             "opcoes": ["A) <td>", "B) <th>", "C) <header>", "D) <head-cell>"], 
             "resposta": "B", "capitulo": 6},
            {"pergunta": "Qual tag agrupa o corpo principal de uma tabela?", 
             "opcoes": ["A) <body>", "B) <table-body>", "C) <tbody>", "D) <main>"], 
             "resposta": "C", "capitulo": 6},
            {"pergunta": "Qual tag cria uma linha de tabela?", 
             "opcoes": ["A) <row>", "B) <tr>", "C) <line>", "D) <table-row>"], 
             "resposta": "B", "capitulo": 6}
        ]
    }
    
    if curso == "HTML":
        biblioteca = {
            1: ("CAPÍTULO 1 - ESTRUTURA BÁSICA DE UM DOCUMENTO HTML", 
                "Um documento HTML é a base de qualquer página web e possui uma estrutura definida que organiza \n "
                "o conteúdo e os metadados de forma lógica e acessível. Esta estrutura básica é composta por uma \n "
                "série de elementos que devem ser organizados corretamente para garantir que a página seja exibida \n "
                "corretamente pelos navegadores.\n\n"
                "Exemplo de estrutura básica:\n\n"
                "<!DOCTYPE html>\n"
                "<html lang='pt-br'>\n"
                "  <head>\n"
                "    <meta charset='UTF-8'>\n"
                "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
                "    <title>Título do Documento</title>\n"
                "  </head>\n"
                "  <body>\n"
                "    Corpo do Documento\n"
                "  </body>\n"
                "</html>\n\n"
                "Explicação das principais tags:\n"
                "- <!DOCTYPE html> → Informa ao navegador que o documento está usando HTML5.\n"
                "- <html lang='pt-br'> → Indica o idioma principal do documento.\n"
                "- <head> </head> → Delimita o cabeçalho, onde ficam metadados e configurações.\n"
                "- <meta charset='UTF-8'> → Define o conjunto de caracteres usado no documento.\n"
                "- <meta name='viewport'...> → Garante que o site seja exibido corretamente em dispositivos móveis.\n"
                "- <title> </title> → Define o título da página (aparece na aba do navegador).\n"
                "- <body> </body> → Contém todo o conteúdo visível da página.\n\n"
                "Agora que você conhece a estrutura básica de um documento HTML, pode começar a entender as "
                "diversas tags que compõem uma página."),
            2: ("CAPÍTULO 2 - TAGS BÁSICAS",
                "As tags estruturais são usadas para organizar o conteúdo de uma página HTML de forma semântica, "
                "facilitando a leitura para os navegadores, mecanismos de busca e leitores de tela. Elas ajudam a "
                "dividir o conteúdo em seções lógicas.\n\n"
                "Principais tags estruturais:\n"
                "- <header> → Representa o cabeçalho de uma página ou seção. Geralmente contém logo, título e menus.\n"
                "- <nav> → Define a área de navegação, como menus e links importantes.\n"
                "- <main> → Indica o conteúdo principal da página, único por documento.\n"
                "- <section> → Agrupa conteúdo relacionado em seções.\n"
                "- <article> → Representa um conteúdo independente, como uma postagem de blog ou notícia.\n"
                "- <aside> → Usado para conteúdos laterais ou complementares, como uma barra lateral.\n"
                "- <footer> → Representa o rodapé da página ou seção, geralmente contém créditos e informações de contato.\n\n"
                "Exemplo de uso:\n\n"
                "<!DOCTYPE html>\n"
                "<html lang='pt-br'>\n"
                "  <head>\n"
                "    <meta charset='UTF-8'>\n"
                "    <title>Exemplo Estrutural</title>\n"
                "  </head>\n"
                "  <body>\n"
                "    <header>\n"
                "      <h1>Meu Site</h1>\n"
                "      <nav>\n"
                "        <a href='#'>Home</a> | <a href='#'>Sobre</a> | <a href='#'>Contato</a>\n"
                "      </nav>\n"
                "    </header>\n"
                "    <main>\n"
                "      <section>\n"
                "        <article>\n"
                "          <h2>Notícia Importante</h2>\n"
                "          <p>Este é o conteúdo da notícia...</p>\n"
                "        </article>\n"
                "      </section>\n"
                "      <aside>\n"
                "        <p>Conteúdo complementar, como links ou anúncios.</p>\n"
                "      </aside>\n"
                "    </main>\n"
                "    <footer>\n"
                "      <p>&copy; 2025 - Meu Site</p>\n"
                "    </footer>\n"
                "  </body>\n"
                "</html>\n\n"
                "Observação: Utilizar essas tags de forma correta melhora a acessibilidade e o SEO (otimização para mecanismos de busca), "
                "além de deixar o código mais organizado e fácil de manter."),
            3: ("CAPÍTULO 3 - FORMULÁRIOS",
                "Os formulários são elementos essenciais para interação do usuário com páginas web. "
                "Eles permitem coletar informações, realizar cadastros, fazer login e muito mais.\n\n"
                "ESTRUTURA BÁSICA DE UM FORMULÁRIO:\n"
                "<form action='processar.php' method='post'>\n"
                "  <!-- Campos do formulário aqui -->\n"
                "</form>\n\n"
                "PRINCIPAIS TIPOS DE INPUT:\n\n"
                "1. CAMPO DE TEXTO:\n"
                "<input type='text' name='nome' placeholder='Digite seu nome' required>\n\n"
                "2. EMAIL:\n"
                "<input type='email' name='email' placeholder='seu@email.com' required>\n\n"
                "3. SENHA:\n"
                "<input type='password' name='senha' placeholder='Sua senha' required>\n\n"
                "4. NÚMERO:\n"
                "<input type='number' name='idade' min='18' max='100' placeholder='Idade'>\n\n"
                "5. DATA:\n"
                "<input type='date' name='nascimento'>\n\n"
                "6. TELEFONE:\n"
                "<input type='tel' name='telefone' placeholder='(11) 99999-9999'>\n\n"
                "7. CHECKBOX (múltipla escolha):\n"
                "<input type='checkbox' name='hobbies' value='leitura'> Leitura\n"
                "<input type='checkbox' name='hobbies' value='esportes'> Esportes\n\n"
                "8. RADIO BUTTON (escolha única):\n"
                "<input type='radio' name='genero' value='masculino'> Masculino\n"
                "<input type='radio' name='genero' value='feminino'> Feminino\n\n"
                "ELEMENTOS AVANÇADOS:\n\n"
                "9. SELECT (lista suspensa):\n"
                "<select name='cidade'>\n"
                "  <option value=''>Escolha uma cidade</option>\n"
                "  <option value='sp'>São Paulo</option>\n"
                "  <option value='rj'>Rio de Janeiro</option>\n"
                "</select>\n\n"
                "10. TEXTAREA (texto longo):\n"
                "<textarea name='mensagem' rows='5' cols='30' placeholder='Sua mensagem'></textarea>\n\n"
                "11. BOTÕES:\n"
                "<button type='submit'>Enviar</button>\n"
                "<button type='reset'>Limpar</button>\n"
                "<input type='submit' value='Cadastrar'>\n\n"
                "EXEMPLO COMPLETO - FORMULÁRIO DE CONTATO:\n\n"
                "<form action='contato.php' method='post'>\n"
                "  <fieldset>\n"
                "    <legend>Dados Pessoais</legend>\n"
                "    \n"
                "    <label for='nome'>Nome Completo:</label>\n"
                "    <input type='text' id='nome' name='nome' required>\n"
                "    \n"
                "    <label for='email'>E-mail:</label>\n"
                "    <input type='email' id='email' name='email' required>\n"
                "    \n"
                "    <label for='telefone'>Telefone:</label>\n"
                "    <input type='tel' id='telefone' name='telefone'>\n"
                "  </fieldset>\n"
                "  \n"
                "  <fieldset>\n"
                "    <legend>Preferências</legend>\n"
                "    \n"
                "    <label for='assunto'>Assunto:</label>\n"
                "    <select id='assunto' name='assunto'>\n"
                "      <option value='duvida'>Dúvida</option>\n"
                "      <option value='sugestao'>Sugestão</option>\n"
                "      <option value='reclamacao'>Reclamação</option>\n"
                "    </select>\n"
                "    \n"
                "    <label>Contato preferido:</label>\n"
                "    <input type='radio' id='email_pref' name='contato' value='email'>\n"
                "    <label for='email_pref'>E-mail</label>\n"
                "    \n"
                "    <input type='radio' id='tel_pref' name='contato' value='telefone'>\n"
                "    <label for='tel_pref'>Telefone</label>\n"
                "  </fieldset>\n"
                "  \n"
                "  <label for='mensagem'>Mensagem:</label>\n"
                "  <textarea id='mensagem' name='mensagem' rows='5' required></textarea>\n"
                "  \n"
                "  <input type='checkbox' id='newsletter' name='newsletter'>\n"
                "  <label for='newsletter'>Desejo receber newsletter</label>\n"
                "  \n"
                "  <button type='submit'>Enviar Mensagem</button>\n"
                "  <button type='reset'>Limpar Formulário</button>\n"
                "</form>\n\n"
                "ATRIBUTOS IMPORTANTES:\n"
                "- required: torna o campo obrigatório\n"
                "- placeholder: texto de exemplo no campo\n"
                "- maxlength: limite de caracteres\n"
                "- min/max: valores mínimo e máximo para números\n"
                "- pattern: validação com expressão regular\n"
                "- disabled: desabilita o campo\n"
                "- readonly: campo apenas para leitura\n\n"
                "DICAS DE ACESSIBILIDADE:\n"
                "- Use <label> para todos os campos\n"
                "- Agrupe campos relacionados com <fieldset> e <legend>\n"
                "- Forneça instruções claras\n"
                "- Use atributos de validação HTML5\n\n"
                "Os formulários são fundamentais para criar interatividade e coletar dados dos usuários de forma organizada e acessível."),
            4: ("CAPÍTULO 4 - LISTAS E LINKS",
                "Neste capítulo, você aprenderá a criar listas e links para estruturar informações e navegação.\n\n"
                "LISTAS:\n"
                "1. Lista não ordenada (<ul>):\n"
                "<ul>\n"
                "  <li>Item 1</li>\n"
                "  <li>Item 2</li>\n"
                "  <li>Item 3</li>\n"
                "</ul>\n\n"
                "2. Lista ordenada (<ol>):\n"
                "<ol>\n"
                "  <li>Primeiro passo</li>\n"
                "  <li>Segundo passo</li>\n"
                "  <li>Terceiro passo</li>\n"
                "</ol>\n\n"
                "3. Lista de definição (<dl>):\n"
                "<dl>\n"
                "  <dt>HTML</dt>\n"
                "  <dd>Linguagem de marcação para páginas web.</dd>\n"
                "</dl>\n\n"
                "LINKS:\n"
                "<a href='https://www.unip.br/cursos/graduacao/index.aspx' target='_blank'>Visite nosso site</a>\n"
                "- href: destino do link\n"
                "- target='_blank': abre em nova aba\n\n"
                "Exemplo prático:\n"
                "<ul>\n"
                "  <li><a href='index.html'>Página Inicial</a></li>\n"
                "  <li><a href='sobre.html'>Sobre</a></li>\n"
                "  <li><a href='contato.html' target='_blank'>Contato</a></li>\n"
                "</ul>"),
            5: ("CAPÍTULO 5 - IMAGENS E MULTIMÍDIA",
                "Aqui veremos como adicionar imagens, áudio e vídeo em uma página HTML.\n\n"
                "IMAGENS:\n"
                "<img src='imagem.jpg' alt='Descrição' width='300'>\n\n"
                "ÁUDIO:\n"
                "<audio controls>\n"
                "  <source src='musica.mp3' type='audio/mpeg'>\n"
                "  Seu navegador não suporta áudio.\n"
                "</audio>\n\n"
                "VÍDEO:\n"
                "<video controls width='400'>\n"
                "  <source src='video.mp4' type='video/mp4'>\n"
                "  Seu navegador não suporta vídeo.\n"
                "</video>\n\n"
                "FIGURA COM LEGENDA:\n"
                "<figure>\n"
                "  <img src='gato.png' alt='Gato fofo'>\n"
                "  <figcaption>Figura 1: Gato dormindo</figcaption>\n"
                "</figure>"),
            6: ("CAPÍTULO 6 - TABELAS",
                "Tabelas organizam informações em linhas e colunas.\n\n"
                "TABELA BÁSICA:\n"
                "<table border='1'>\n"
                "  <tr>\n"
                "    <th>Nome</th><th>Idade</th>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>Ana</td><td>25</td>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>João</td><td>30</td>\n"
                "  </tr>\n"
                "</table>\n\n"
                "TABELA COM CABEÇALHO, CORPO E RODAPÉ:\n"
                "<table border='1'>\n"
                "  <thead>\n"
                "    <tr><th>Produto</th><th>Preço</th></tr>\n"
                "  </thead>\n"
                "  <tbody>\n"
                "    <tr><td>Mouse</td><td>R$ 50,00</td></tr>\n"
                "    <tr><td>Teclado</td><td>R$ 80,00</td></tr>\n"
                "  </tbody>\n"
                "  <tfoot>\n"
                "    <tr><td>Total</td><td>R$ 130,00</td></tr>\n"
                "  </tfoot>\n"
                "</table>")
        }
        
    elif curso == "CSS":
        biblioteca = {
            1: ("CAPÍTULO 1 - INTRODUÇÃO AO CSS",
                "CSS (Cascading Style Sheets) é a linguagem usada para estilizar páginas HTML. "
                "Ela controla a aparência, layout e design dos elementos web.\n\n"
                "FORMAS DE APLICAR CSS:\n\n"
                "1. CSS INLINE (dentro da tag):\n"
                "<p style='color: blue; font-size: 18px;'>Texto azul</p>\n\n"
                "2. CSS INTERNO (na tag <style>):\n"
                "<style>\n"
                "  p { color: blue; font-size: 18px; }\n"
                "</style>\n\n"
                "3. CSS EXTERNO (arquivo separado):\n"
                "<link rel='stylesheet' href='estilo.css'>\n\n"
                "SELETORES BÁSICOS:\n\n"
                "• Seletor de elemento: p { color: red; }\n"
                "• Seletor de classe: .destaque { font-weight: bold; }\n"
                "• Seletor de ID: #titulo { font-size: 24px; }\n"
                "• Seletor universal: * { margin: 0; }\n\n"
                "PROPRIEDADES FUNDAMENTAIS:\n\n"
                "CORES:\n"
                "color: red; /* cor do texto */\n"
                "background-color: #ff0000; /* cor de fundo */\n"
                "background-color: rgb(255, 0, 0); /* RGB */\n"
                "background-color: rgba(255, 0, 0, 0.5); /* com transparência */\n\n"
                "TEXTO:\n"
                "font-family: Arial, sans-serif;\n"
                "font-size: 16px;\n"
                "font-weight: bold;\n"
                "text-align: center;\n"
                "text-decoration: underline;\n\n"
                "EXEMPLO PRÁTICO:\n\n"
                "HTML:\n"
                "<h1 class='titulo'>Meu Site</h1>\n"
                "<p id='introducao'>Bem-vindo ao meu site!</p>\n"
                "<p class='destaque'>Conteúdo importante</p>\n\n"
                "CSS:\n"
                ".titulo {\n"
                "  color: #2c3e50;\n"
                "  font-family: 'Arial', sans-serif;\n"
                "  text-align: center;\n"
                "  margin-bottom: 20px;\n"
                "}\n\n"
                "#introducao {\n"
                "  font-size: 18px;\n"
                "  color: #7f8c8d;\n"
                "  line-height: 1.5;\n"
                "}\n\n"
                ".destaque {\n"
                "  background-color: #f39c12;\n"
                "  color: white;\n"
                "  padding: 10px;\n"
                "  border-radius: 5px;\n"
                "}"),
            2: ("CAPÍTULO 2 - BOX MODEL E LAYOUT",
                "O Box Model é fundamental no CSS. Todo elemento HTML é uma caixa com conteúdo, "
                "padding, border e margin.\n\n"
                "ESTRUTURA DO BOX MODEL:\n"
                "┌─────────────────────────────────┐\n"
                "│           MARGIN                │\n"
                "│  ┌─────────────────────────────┐ │\n"
                "│  │         BORDER              │ │\n"
                "│  │  ┌─────────────────────────┐ │ │\n"
                "│  │  │       PADDING           │ │ │\n"
                "│  │  │  ┌─────────────────────┐ │ │ │\n"
                "│  │  │  │     CONTENT         │ │ │ │\n"
                "│  │  │  └─────────────────────┘ │ │ │\n"
                "│  │  └─────────────────────────┘ │ │\n"
                "│  └─────────────────────────────┘ │\n"
                "└─────────────────────────────────┘\n\n"
                "PROPRIEDADES DO BOX MODEL:\n\n"
                "WIDTH E HEIGHT:\n"
                "width: 300px; /* largura */\n"
                "height: 200px; /* altura */\n"
                "max-width: 100%; /* largura máxima */\n"
                "min-height: 150px; /* altura mínima */\n\n"
                "PADDING (espaçamento interno):\n"
                "padding: 20px; /* todos os lados */\n"
                "padding: 10px 20px; /* vertical horizontal */\n"
                "padding: 10px 15px 20px 25px; /* top right bottom left */\n"
                "padding-top: 10px; /* apenas topo */\n\n"
                "MARGIN (espaçamento externo):\n"
                "margin: 20px; /* todos os lados */\n"
                "margin: 0 auto; /* centralizar horizontalmente */\n"
                "margin-bottom: 30px; /* apenas embaixo */\n\n"
                "BORDER (borda):\n"
                "border: 2px solid #333; /* espessura estilo cor */\n"
                "border-radius: 10px; /* bordas arredondadas */\n"
                "border-top: 1px dashed red; /* apenas topo */\n\n"
                "DISPLAY:\n"
                "display: block; /* elemento em bloco */\n"
                "display: inline; /* elemento em linha */\n"
                "display: inline-block; /* híbrido */\n"
                "display: none; /* ocultar elemento */\n\n"
                "POSITION:\n"
                "position: static; /* padrão */\n"
                "position: relative; /* relativo à posição original */\n"
                "position: absolute; /* relativo ao pai posicionado */\n"
                "position: fixed; /* fixo na tela */\n"
                "top: 10px; left: 20px; /* coordenadas */\n\n"
                "EXEMPLO PRÁTICO - CARD:\n\n"
                ".card {\n"
                "  width: 300px;\n"
                "  background-color: white;\n"
                "  border: 1px solid #ddd;\n"
                "  border-radius: 8px;\n"
                "  padding: 20px;\n"
                "  margin: 20px auto;\n"
                "  box-shadow: 0 2px 4px rgba(0,0,0,0.1);\n"
                "}\n\n"
                ".card h3 {\n"
                "  margin-top: 0;\n"
                "  color: #333;\n"
                "}\n\n"
                ".card p {\n"
                "  line-height: 1.6;\n"
                "  color: #666;\n"
                "  margin-bottom: 0;\n"
                "}"),
            3: ("CAPÍTULO 3 - FLEXBOX E GRID",
                "Flexbox e Grid são sistemas de layout modernos que facilitam a criação de "
                "layouts responsivos e alinhamentos complexos.\n\n"
                "FLEXBOX - LAYOUT UNIDIMENSIONAL:\n\n"
                "CONTAINER FLEX (pai):\n"
                ".container {\n"
                "  display: flex;\n"
                "  flex-direction: row; /* row, column, row-reverse, column-reverse */\n"
                "  justify-content: center; /* main axis: flex-start, center, flex-end, space-between, space-around */\n"
                "  align-items: center; /* cross axis: flex-start, center, flex-end, stretch */\n"
                "  flex-wrap: wrap; /* nowrap, wrap, wrap-reverse */\n"
                "  gap: 20px; /* espaçamento entre itens */\n"
                "}\n\n"
                "ITENS FLEX (filhos):\n"
                ".item {\n"
                "  flex: 1; /* grow shrink basis */\n"
                "  flex-grow: 1; /* cresce para preencher espaço */\n"
                "  flex-shrink: 0; /* não encolhe */\n"
                "  flex-basis: 200px; /* tamanho base */\n"
                "  align-self: flex-end; /* alinhamento individual */\n"
                "}\n\n"
                "EXEMPLO FLEXBOX - NAVBAR:\n\n"
                "HTML:\n"
                "<nav class='navbar'>\n"
                "  <div class='logo'>MeuSite</div>\n"
                "  <ul class='menu'>\n"
                "    <li><a href='#'>Home</a></li>\n"
                "    <li><a href='#'>Sobre</a></li>\n"
                "    <li><a href='#'>Contato</a></li>\n"
                "  </ul>\n"
                "</nav>\n\n"
                "CSS:\n"
                ".navbar {\n"
                "  display: flex;\n"
                "  justify-content: space-between;\n"
                "  align-items: center;\n"
                "  padding: 1rem 2rem;\n"
                "  background-color: #333;\n"
                "}\n\n"
                ".menu {\n"
                "  display: flex;\n"
                "  list-style: none;\n"
                "  gap: 2rem;\n"
                "  margin: 0;\n"
                "}\n\n"
                "CSS GRID - LAYOUT BIDIMENSIONAL:\n\n"
                "CONTAINER GRID:\n"
                ".grid-container {\n"
                "  display: grid;\n"
                "  grid-template-columns: 1fr 2fr 1fr; /* 3 colunas */\n"
                "  grid-template-rows: auto 1fr auto; /* 3 linhas */\n"
                "  grid-gap: 20px; /* espaçamento */\n"
                "  height: 100vh;\n"
                "}\n\n"
                "POSICIONAMENTO DE ITENS:\n"
                ".header {\n"
                "  grid-column: 1 / -1; /* ocupa todas as colunas */\n"
                "  grid-row: 1;\n"
                "}\n\n"
                ".sidebar {\n"
                "  grid-column: 1;\n"
                "  grid-row: 2;\n"
                "}\n\n"
                ".main {\n"
                "  grid-column: 2;\n"
                "  grid-row: 2;\n"
                "}\n\n"
                "EXEMPLO GRID - LAYOUT COMPLETO:\n\n"
                ".page-layout {\n"
                "  display: grid;\n"
                "  grid-template-areas:\n"
                "    'header header header'\n"
                "    'sidebar main aside'\n"
                "    'footer footer footer';\n"
                "  grid-template-columns: 200px 1fr 150px;\n"
                "  grid-template-rows: auto 1fr auto;\n"
                "  min-height: 100vh;\n"
                "  gap: 1rem;\n"
                "}\n\n"
                ".header { grid-area: header; }\n"
                ".sidebar { grid-area: sidebar; }\n"
                ".main { grid-area: main; }\n"
                ".aside { grid-area: aside; }\n"
                ".footer { grid-area: footer; }")
        }
    else:  # LÓGICA DE PROGRAMAÇÃO
        biblioteca = {
            1: ("CAPÍTULO 1 - INTRODUÇÃO À LÓGICA DE PROGRAMAÇÃO",
                "A lógica de programação é a base fundamental para resolver problemas através de "
                "algoritmos e estruturas de pensamento organizadas.\n\n"
                "O QUE É LÓGICA DE PROGRAMAÇÃO?\n\n"
                "É a capacidade de organizar o pensamento de forma sequencial e lógica para "
                "resolver problemas, dividindo-os em etapas menores e mais simples.\n\n"
                "CONCEITOS FUNDAMENTAIS:\n\n"
                "1. ALGORITMO:\n"
                "Sequência finita de passos para resolver um problema.\n\n"
                "Exemplo - Fazer um sanduíche:\n"
                "1. Pegar 2 fatias de pão\n"
                "2. Passar manteiga no pão\n"
                "3. Colocar o recheio\n"
                "4. Fechar o sanduíche\n"
                "5. Servir\n\n"
                "2. VARIÁVEIS:\n"
                "Espaços na memória para armazenar dados que podem mudar.\n\n"
                "Exemplo:\n"
                "nome = 'João'\n"
                "idade = 25\n"
                "altura = 1.75\n"
                "estudante = True\n\n"
                "TIPOS DE DADOS:\n"
                "• Inteiro: 10, -5, 0\n"
                "• Real/Float: 3.14, -2.5, 0.0\n"
                "• Texto/String: 'Olá', 'Python', '123'\n"
                "• Lógico/Boolean: True, False\n\n"
                "3. OPERADORES:\n\n"
                "ARITMÉTICOS:\n"
                "+ (soma): 5 + 3 = 8\n"
                "- (subtração): 10 - 4 = 6\n"
                "* (multiplicação): 3 * 4 = 12\n"
                "/ (divisão): 15 / 3 = 5\n"
                "% (resto): 10 % 3 = 1\n"
                "** (potência): 2 ** 3 = 8\n\n"
                "RELACIONAIS:\n"
                "== (igual): 5 == 5 → True\n"
                "!= (diferente): 3 != 5 → True\n"
                "> (maior): 8 > 3 → True\n"
                "< (menor): 2 < 7 → True\n"
                ">= (maior ou igual): 5 >= 5 → True\n"
                "<= (menor ou igual): 3 <= 4 → True\n\n"
                "LÓGICOS:\n"
                "and (E): True and False → False\n"
                "or (OU): True or False → True\n"
                "not (NÃO): not True → False\n\n"
                "EXEMPLO PRÁTICO - CALCULADORA SIMPLES:\n\n"
                "# Entrada de dados\n"
                "numero1 = float(input('Digite o primeiro número: '))\n"
                "operacao = input('Digite a operação (+, -, *, /): ')\n"
                "numero2 = float(input('Digite o segundo número: '))\n\n"
                "# Processamento\n"
                "if operacao == '+':\n"
                "    resultado = numero1 + numero2\n"
                "elif operacao == '-':\n"
                "    resultado = numero1 - numero2\n"
                "elif operacao == '*':\n"
                "    resultado = numero1 * numero2\n"
                "elif operacao == '/' and numero2 != 0:\n"
                "    resultado = numero1 / numero2\n"
                "else:\n"
                "    resultado = 'Operação inválida'\n\n"
                "# Saída\n"
                "print(f'Resultado: {resultado}')"),
            2: ("CAPÍTULO 2 - ESTRUTURAS DE CONTROLE",
                "As estruturas de controle permitem alterar o fluxo de execução do programa "
                "baseado em condições e repetições.\n\n"
                "1. ESTRUTURAS CONDICIONAIS:\n\n"
                "IF SIMPLES:\n"
                "if condição:\n"
                "    # código executado se condição for verdadeira\n"
                "    print('Condição verdadeira')\n\n"
                "Exemplo:\n"
                "idade = 18\n"
                "if idade >= 18:\n"
                "    print('Maior de idade')\n\n"
                "IF-ELSE:\n"
                "if condição:\n"
                "    # código se verdadeiro\n"
                "else:\n"
                "    # código se falso\n\n"
                "Exemplo:\n"
                "nota = 7.5\n"
                "if nota >= 7.0:\n"
                "    print('Aprovado')\n"
                "else:\n"
                "    print('Reprovado')\n\n"
                "IF-ELIF-ELSE (múltiplas condições):\n"
                "if condição1:\n"
                "    # código 1\n"
                "elif condição2:\n"
                "    # código 2\n"
                "elif condição3:\n"
                "    # código 3\n"
                "else:\n"
                "    # código padrão\n\n"
                "Exemplo - Sistema de notas:\n"
                "nota = float(input('Digite sua nota: '))\n\n"
                "if nota >= 9.0:\n"
                "    conceito = 'A - Excelente'\n"
                "elif nota >= 8.0:\n"
                "    conceito = 'B - Muito Bom'\n"
                "elif nota >= 7.0:\n"
                "    conceito = 'C - Bom'\n"
                "elif nota >= 6.0:\n"
                "    conceito = 'D - Regular'\n"
                "else:\n"
                "    conceito = 'F - Insuficiente'\n\n"
                "print(f'Seu conceito: {conceito}')\n\n"
                "2. ESTRUTURAS DE REPETIÇÃO:\n\n"
                "FOR (repetição com contador):\n"
                "for variavel in range(inicio, fim, passo):\n"
                "    # código a repetir\n\n"
                "Exemplos:\n"
                "# Contar de 1 a 5\n"
                "for i in range(1, 6):\n"
                "    print(f'Número: {i}')\n\n"
                "# Tabuada do 5\n"
                "for i in range(1, 11):\n"
                "    resultado = 5 * i\n"
                "    print(f'5 x {i} = {resultado}')\n\n"
                "WHILE (repetição com condição):\n"
                "while condição:\n"
                "    # código a repetir\n"
                "    # atualizar variável de controle\n\n"
                "Exemplo - Contador:\n"
                "contador = 1\n"
                "while contador <= 5:\n"
                "    print(f'Contagem: {contador}')\n"
                "    contador += 1  # contador = contador + 1\n\n"
                "Exemplo - Menu com repetição:\n"
                "opcao = 0\n"
                "while opcao != 4:\n"
                "    print('1 - Cadastrar')\n"
                "    print('2 - Listar')\n"
                "    print('3 - Excluir')\n"
                "    print('4 - Sair')\n"
                "    opcao = int(input('Escolha: '))\n"
                "    \n"
                "    if opcao == 1:\n"
                "        print('Cadastrando...')\n"
                "    elif opcao == 2:\n"
                "        print('Listando...')\n"
                "    elif opcao == 3:\n"
                "        print('Excluindo...')\n"
                "    elif opcao == 4:\n"
                "        print('Saindo...')\n"
                "    else:\n"
                "        print('Opção inválida!')\n\n"
                "CONTROLE DE FLUXO:\n"
                "• break: sai do loop\n"
                "• continue: pula para próxima iteração\n\n"
                "Exemplo:\n"
                "for i in range(1, 11):\n"
                "    if i == 5:\n"
                "        continue  # pula o 5\n"
                "    if i == 8:\n"
                "        break     # para no 8\n"
                "    print(i)  # imprime: 1, 2, 3, 4, 6, 7"),
            3: ("CAPÍTULO 3 - ESTRUTURAS DE DADOS E FUNÇÕES",
                "Estruturas de dados organizam informações, e funções organizam código "
                "para reutilização e modularização.\n\n"
                "1. LISTAS (ARRAYS):\n\n"
                "CRIAÇÃO E ACESSO:\n"
                "# Criar lista\n"
                "frutas = ['maçã', 'banana', 'laranja', 'uva']\n"
                "numeros = [1, 2, 3, 4, 5]\n"
                "mista = ['João', 25, True, 1.75]\n\n"
                "# Acessar elementos (índice começa em 0)\n"
                "print(frutas[0])    # 'maçã'\n"
                "print(frutas[-1])   # 'uva' (último elemento)\n"
                "print(frutas[1:3])  # ['banana', 'laranja'] (fatia)\n\n"
                "OPERAÇÕES COM LISTAS:\n"
                "# Adicionar elementos\n"
                "frutas.append('pêra')           # adiciona no final\n"
                "frutas.insert(1, 'manga')       # adiciona na posição 1\n\n"
                "# Remover elementos\n"
                "frutas.remove('banana')         # remove por valor\n"
                "fruta_removida = frutas.pop()   # remove e retorna o último\n"
                "del frutas[0]                   # remove por índice\n\n"
                "# Outras operações\n"
                "print(len(frutas))              # tamanho da lista\n"
                "print('maçã' in frutas)         # verifica se existe\n"
                "frutas.sort()                   # ordena a lista\n"
                "frutas.reverse()                # inverte a ordem\n\n"
                "PERCORRER LISTAS:\n"
                "# Método 1 - por elemento\n"
                "for fruta in frutas:\n"
                "    print(f'Fruta: {fruta}')\n\n"
                "# Método 2 - por índice\n"
                "for i in range(len(frutas)):\n"
                "    print(f'Posição {i}: {frutas[i]}')\n\n"
                "# Método 3 - com enumerate\n"
                "for i, fruta in enumerate(frutas):\n"
                "    print(f'Posição {i}: {fruta}')\n\n"
                "2. DICIONÁRIOS:\n\n"
                "CRIAÇÃO E ACESSO:\n"
                "# Criar dicionário\n"
                "pessoa = {\n"
                "    'nome': 'Ana',\n"
                "    'idade': 28,\n"
                "    'cidade': 'São Paulo',\n"
                "    'profissao': 'Engenheira'\n"
                "}\n\n"
                "# Acessar valores\n"
                "print(pessoa['nome'])           # 'Ana'\n"
                "print(pessoa.get('idade'))      # 28\n"
                "print(pessoa.get('salario', 0)) # 0 (valor padrão)\n\n"
                "# Modificar e adicionar\n"
                "pessoa['idade'] = 29            # modifica\n"
                "pessoa['salario'] = 5000        # adiciona nova chave\n\n"
                "# Percorrer dicionário\n"
                "for chave, valor in pessoa.items():\n"
                "    print(f'{chave}: {valor}')\n\n"
                "3. FUNÇÕES:\n\n"
                "DEFINIÇÃO E USO:\n"
                "def nome_da_funcao(parametros):\n"
                "    # código da função\n"
                "    return valor  # opcional\n\n"
                "# Função simples\n"
                "def saudacao():\n"
                "    print('Olá, mundo!')\n\n"
                "# Chamar função\n"
                "saudacao()  # executa a função\n\n"
                "FUNÇÕES COM PARÂMETROS:\n"
                "def saudacao_personalizada(nome):\n"
                "    print(f'Olá, {nome}!')\n\n"
                "def somar(a, b):\n"
                "    resultado = a + b\n"
                "    return resultado\n\n"
                "# Usar as funções\n"
                "saudacao_personalizada('Maria')\n"
                "soma = somar(5, 3)\n"
                "print(f'Soma: {soma}')\n\n"
                "EXEMPLO COMPLETO - SISTEMA DE CADASTRO:\n\n"
                "# Lista para armazenar pessoas\n"
                "pessoas = []\n\n"
                "def cadastrar_pessoa():\n"
                "    nome = input('Nome: ')\n"
                "    idade = int(input('Idade: '))\n"
                "    cidade = input('Cidade: ')\n"
                "    \n"
                "    pessoa = {\n"
                "        'nome': nome,\n"
                "        'idade': idade,\n"
                "        'cidade': cidade\n"
                "    }\n"
                "    \n"
                "    pessoas.append(pessoa)\n"
                "    print('Pessoa cadastrada com sucesso!')\n\n"
                "def listar_pessoas():\n"
                "    if len(pessoas) == 0:\n"
                "        print('Nenhuma pessoa cadastrada.')\n"
                "        return\n"
                "    \n"
                "    for i, pessoa in enumerate(pessoas, 1):\n"
                "        print(f'{i}. {pessoa[\"nome\"]} - {pessoa[\"idade\"]} anos - {pessoa[\"cidade\"]}')\n\n"
                "def buscar_pessoa(nome_busca):\n"
                "    for pessoa in pessoas:\n"
                "        if pessoa['nome'].lower() == nome_busca.lower():\n"
                "            return pessoa\n"
                "    return None\n\n"
                "# Menu principal\n"
                "while True:\n"
                "    print('\\n1 - Cadastrar')\n"
                "    print('2 - Listar')\n"
                "    print('3 - Buscar')\n"
                "    print('4 - Sair')\n"
                "    \n"
                "    opcao = input('Escolha: ')\n"
                "    \n"
                "    if opcao == '1':\n"
                "        cadastrar_pessoa()\n"
                "    elif opcao == '2':\n"
                "        listar_pessoas()\n"
                "    elif opcao == '3':\n"
                "        nome = input('Nome para buscar: ')\n"
                "        pessoa = buscar_pessoa(nome)\n"
                "        if pessoa:\n"
                "            print(f'Encontrado: {pessoa}')\n"
                "        else:\n"
                "            print('Pessoa não encontrada.')\n"
                "    elif opcao == '4':\n"
                "        break\n"
                "    else:\n"
                "        print('Opção inválida!')")
        }

    while True:
        print("\nESCOLHA UMA OPÇÃO:")
        print("[1] ESTUDAR")
        print("[2] FAZER AVALIAÇÃO")
        print("[3] ESCOLHER OUTRO CURSO")
        print("[4] SAIR")
        
        try:
            opcao = int(input("Digite sua opção: "))

            if opcao == 1:
                if curso == "HTML":
                    estudar_capitulos(biblioteca, curso, quiz_html)
                elif curso == "CSS":
                    estudar_capitulos(biblioteca, curso, quiz_css)
                else:  # LÓGICA DE PROGRAMAÇÃO
                    estudar_capitulos(biblioteca, curso, quiz_logica)

            elif opcao == 2:
                if curso == "HTML":
                    fazer_quiz_html(quiz_html, biblioteca)
                elif curso == "CSS":
                    fazer_quiz_css(quiz_css, biblioteca)
                else:  # LÓGICA DE PROGRAMAÇÃO
                    fazer_quiz_logica(quiz_logica, biblioteca)

            elif opcao == 3:
                print("🔄 Voltando para seleção de cursos...")
                unitech()  # Reinicia o programa
                return

            elif opcao == 4:
                print("\nATÉ LOGO!")
                break

            else:
                print("❌ Opção inválida, tente novamente.")
                
        except ValueError:
            print("❌ Digite apenas números de 1 a 4.")

# Executa o programa
unitech()
