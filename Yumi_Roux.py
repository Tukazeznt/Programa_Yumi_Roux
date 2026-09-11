import flet as ft
import random


def main(page: ft.Page):

    # =========================
    # CONFIGURAÇÃO
    # =========================

    page.title = "Yumi_Roux | Meta City"
    page.bgcolor = "#0b0b10"
    page.padding = 0
    page.spacing = 0

    # Compatibilidade com versões diferentes do Flet
    try:
        page.window.width = 1200
        page.window.height = 750
    except Exception:
        try:
            page.window_width = 1200
            page.window_height = 750
        except Exception:
            pass

    # =========================
    # DADOS DA PERSONAGEM
    # =========================

    nome = "Yumi_Roux"

    espectadores = 1247
    saldo = 8750.50
    reputacao = 87
    nivel = 24
    xp = 72
    combustivel = 72

    localizacao = "Centro de Meta City"
    veiculo = "Karin Sultan RS"

    # =========================
    # VEÍCULOS
    # =========================

    veiculos = [
        {
            "nome": "Karin Sultan RS",
            "tipo": "Esportivo",
            "combustivel": 72
        },
        {
            "nome": "Nissan Skyline",
            "tipo": "Tuner",
            "combustivel": 91
        },
        {
            "nome": "BMW M4",
            "tipo": "Luxo",
            "combustivel": 45
        }
    ]

    # =========================
    # INVENTÁRIO
    # =========================

    inventario = [
        ["Celular", "📱", 1],
        ["Kit médico", "🩹", 3],
        ["Rádio", "📻", 1],
        ["Dinheiro", "💵", 850]
    ]

    # =========================
    # MISSÕES
    # =========================

    missoes = [
        {
            "nome": "Levar um cliente até Vinewood",
            "recompensa": 850,
            "xp": 20,
            "icone": "🚗",
            "status": "Disponível"
        },
        {
            "nome": "Entregar uma encomenda secreta",
            "recompensa": 1200,
            "xp": 30,
            "icone": "📦",
            "status": "Disponível"
        },
        {
            "nome": "Escapar de uma perseguição policial",
            "recompensa": 1800,
            "xp": 45,
            "icone": "👮",
            "status": "Disponível"
        }
    ]

    # =========================
    # RÁDIO
    # =========================

    radio_musicas = [
        "Meta Nights",
        "Night Drive",
        "City Lights",
        "Midnight FM"
    ]

    radio_index = 0
    radio_tocando = False
    volume = 70

    # =========================
    # ÁREA PRINCIPAL
    # =========================

    conteudo = ft.Column(
        expand=True,
        spacing=15,
        scroll=ft.ScrollMode.AUTO
    )

    titulo_pagina = ft.Text(
        "DASHBOARD",
        size=13,
        color="#777784",
        weight=ft.FontWeight.BOLD
    )

    # =========================
    # ELEMENTOS DINÂMICOS
    # =========================

    espectadores_text = ft.Text(
        f"{espectadores:,}".replace(",", "."),
        size=24,
        weight=ft.FontWeight.BOLD
    )

    saldo_text = ft.Text(
        f"R$ {saldo:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", "."),
        size=24,
        weight=ft.FontWeight.BOLD
    )

    reputacao_text = ft.Text(
        f"{reputacao}%",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    nivel_text = ft.Text(
        f"NÍVEL {nivel}",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    xp_text = ft.Text(
        f"{xp}/100 XP",
        size=12,
        color="#9999a8"
    )

    localizacao_text = ft.Text(
        localizacao,
        size=15
    )

    veiculo_text = ft.Text(
        veiculo,
        size=15
    )

    combustivel_text = ft.Text(
        f"{combustivel}%",
        size=15,
        weight=ft.FontWeight.BOLD
    )

    status_radio_text = ft.Text(
        "PAUSADO",
        size=11,
        color="#777784"
    )

    musica_text = ft.Text(
        radio_musicas[radio_index],
        size=18,
        weight=ft.FontWeight.BOLD
    )

    volume_text = ft.Text(
        f"Volume: {volume}%",
        size=12,
        color="#9999a8"
    )

    missao_dashboard_text = ft.Text(
        "🚗 Levar um cliente até Vinewood",
        size=15,
        weight=ft.FontWeight.BOLD
    )

    # =========================
    # AVISOS
    # =========================

    def aviso(texto):

        try:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(texto)
            )

            page.snack_bar.open = True

        except Exception:
            pass

    # =========================
    # ATUALIZAR ESTATÍSTICAS
    # =========================

    def atualizar_stats():

        espectadores_text.value = (
            f"{espectadores:,}".replace(",", ".")
        )

        saldo_text.value = (
            f"R$ {saldo:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        reputacao_text.value = f"{reputacao}%"

        nivel_text.value = f"NÍVEL {nivel}"

        xp_text.value = f"{xp}/100 XP"

        localizacao_text.value = localizacao

        veiculo_text.value = veiculo

        combustivel_text.value = f"{combustivel}%"

    # =========================
    # SISTEMA DE XP
    # =========================

    def ganhar_xp(valor):

        nonlocal xp
        nonlocal nivel

        xp += valor

        while xp >= 100:

            xp -= 100

            nivel += 1

            aviso(
                f"⭐ LEVEL UP! Agora você está no nível {nivel}."
            )

        atualizar_stats()

    # =========================
    # DASHBOARD
    # =========================

    def atualizar_live(e):

        nonlocal espectadores
        nonlocal reputacao

        espectadores += random.randint(-20, 45)

        if espectadores < 0:
            espectadores = 0

        reputacao += random.choice(
            [-1, 0, 0, 1, 2]
        )

        reputacao = max(
            0,
            min(100, reputacao)
        )

        atualizar_stats()

        aviso(
            "📡 Live atualizada com sucesso!"
        )

        page.update()

    # =========================
    # VEÍCULOS
    # =========================

    def abastecer(e):

        nonlocal combustivel

        combustivel = 100

        for carro in veiculos:

            if carro["nome"] == veiculo:
                carro["combustivel"] = 100

        atualizar_stats()

        aviso(
            "⛽ Veículo abastecido com sucesso!"
        )

        page.update()

    def dirigir(e):

        nonlocal combustivel
        nonlocal localizacao

        if combustivel <= 5:

            aviso(
                "⛽ Combustível insuficiente para dirigir."
            )

            return

        combustivel -= random.randint(
            5,
            15
        )

        locais = [
            "Centro de Meta City",
            "Vinewood",
            "Praia de Meta City",
            "Downtown",
            "Porto de Meta City",
            "Oficina LS"
        ]

        localizacao = random.choice(
            locais
        )

        for carro in veiculos:

            if carro["nome"] == veiculo:
                carro["combustivel"] = combustivel

        ganhar_xp(5)

        atualizar_stats()

        aviso(
            f"🚗 Você dirigiu até {localizacao}."
        )

        page.update()

    def trocar_veiculo(nome_carro):

        nonlocal veiculo
        nonlocal combustivel

        for carro in veiculos:

            if carro["nome"] == nome_carro:

                veiculo = carro["nome"]

                combustivel = carro["combustivel"]

        atualizar_stats()

        aviso(
            f"🚘 Veículo selecionado: {veiculo}"
        )

        mostrar_tela("Veículos")

    # =========================
    # MISSÕES
    # =========================

    def aceitar_missao(indice):

        if missoes[indice]["status"] != "Disponível":

            aviso(
                "Essa missão já foi concluída."
            )

            return

        missoes[indice]["status"] = "Em andamento"

        aviso(
            f"🎯 Missão aceita: "
            f"{missoes[indice]['nome']}"
        )

        mostrar_tela("Missões")

    def concluir_missao(indice):

        nonlocal saldo
        nonlocal reputacao

        if missoes[indice]["status"] != "Em andamento":

            aviso(
                "Aceite a missão antes de concluir."
            )

            return

        recompensa = missoes[indice]["recompensa"]

        ganho_xp = missoes[indice]["xp"]

        saldo += recompensa

        reputacao = min(
            100,
            reputacao + 2
        )

        missoes[indice]["status"] = "Concluída"

        ganhar_xp(
            ganho_xp
        )

        atualizar_stats()

        aviso(
            f"💰 Missão concluída! "
            f"+R$ {recompensa}"
        )

        mostrar_tela("Missões")

    def gerar_nova_missao(e):

        disponiveis = [
            m for m in missoes
            if m["status"] == "Disponível"
        ]

        if disponiveis:

            escolhida = random.choice(
                disponiveis
            )

            missao_dashboard_text.value = (
                f"{escolhida['icone']} "
                f"{escolhida['nome']}"
            )

        else:

            missao_dashboard_text.value = (
                "🏆 Todas as missões "
                "foram concluídas!"
            )

        page.update()

    # =========================
    # INVENTÁRIO
    # =========================

    def adicionar_item(
        nome_item,
        icone
    ):

        for item in inventario:

            if item[0] == nome_item:

                item[2] += 1

                aviso(
                    f"🎒 +1 {nome_item}"
                )

                mostrar_tela(
                    "Inventário"
                )

                return

        inventario.append(
            [
                nome_item,
                icone,
                1
            ]
        )

        aviso(
            f"🎒 {nome_item} "
            "adicionado ao inventário."
        )

        mostrar_tela(
            "Inventário"
        )

    def usar_item(indice):

        item = inventario[indice]

        if item[2] <= 0:

            aviso(
                "Item indisponível."
            )

            return

        item[2] -= 1

        if item[0] == "Kit médico":

            aviso(
                "🩹 Kit médico utilizado."
            )

        elif item[0] == "Celular":

            aviso(
                "📱 Você abriu o celular."
            )

        elif item[0] == "Rádio":

            aviso(
                "📻 Você ligou o rádio."
            )

        else:

            aviso(
                f"✅ {item[0]} utilizado."
            )

        mostrar_tela(
            "Inventário"
        )

    # =========================
    # RÁDIO
    # =========================

    def tocar_radio(e):

        nonlocal radio_tocando

        radio_tocando = not radio_tocando

        if radio_tocando:

            status_radio_text.value = (
                "● TOCANDO"
            )

            status_radio_text.color = (
                "#ff3b81"
            )

            aviso(
                "🎵 Rádio ligada!"
            )

        else:

            status_radio_text.value = (
                "PAUSADO"
            )

            status_radio_text.color = (
                "#777784"
            )

            aviso(
                "⏸ Rádio pausada."
            )

        page.update()

    def proxima_musica(e):

        nonlocal radio_index

        radio_index = (
            radio_index + 1
        ) % len(radio_musicas)

        musica_text.value = (
            radio_musicas[radio_index]
        )

        page.update()

    def musica_anterior(e):

        nonlocal radio_index

        radio_index = (
            radio_index - 1
        ) % len(radio_musicas)

        musica_text.value = (
            radio_musicas[radio_index]
        )

        page.update()

    def aumentar_volume(e):

        nonlocal volume

        volume = min(
            100,
            volume + 10
        )

        volume_text.value = (
            f"Volume: {volume}%"
        )

        page.update()

    def diminuir_volume(e):

        nonlocal volume

        volume = max(
            0,
            volume - 10
        )

        volume_text.value = (
            f"Volume: {volume}%"
        )

        page.update()

    # =========================
    # CHAT
    # =========================

    chat = ft.Column(
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    mensagens = [
        (
            "Mika",
            "YUMI CHEGOU NA META 🔥"
        ),
        (
            "Lucas",
            "vai fazer missão hoje?"
        ),
        (
            "Naty",
            "manda salveeeee ❤️"
        ),
        (
            "Pedro",
            "essa Sultan é linda"
        ),
        (
            "Rafa",
            "YUMI VAI PRA DP KKKKK"
        )
    ]

    for usuario, mensagem in mensagens:

        chat.controls.append(
            ft.Row(
                [
                    ft.Text(
                        usuario,
                        weight=ft.FontWeight.BOLD,
                        size=13
                    ),
                    ft.Text(
                        mensagem,
                        size=13
                    )
                ],
                spacing=8
            )
        )

    mensagem_input = ft.TextField(
        hint_text="Digite uma mensagem...",
        expand=True,
        height=45,
        border_radius=12,
        bgcolor="#15151d",
        border_color="#292936"
    )

    def enviar_mensagem(e):

        texto = mensagem_input.value or ""

        if texto.strip():

            chat.controls.append(
                ft.Row(
                    [
                        ft.Text(
                            "Você",
                            weight=ft.FontWeight.BOLD,
                            size=13
                        ),
                        ft.Text(
                            texto,
                            size=13
                        )
                    ],
                    spacing=8
                )
            )

            mensagem_input.value = ""

            page.update()

    mensagem_input.on_submit = (
        enviar_mensagem
    )

    # =========================
    # COMPONENTES
    # =========================

    def card_stat(
        titulo,
        valor,
        icone
    ):

        return ft.Container(

            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                icone,
                                size=22
                            ),
                            ft.Text(
                                titulo,
                                size=12,
                                color="#9999a8"
                            )
                        ]
                    ),

                    valor
                ],

                spacing=8
            ),

            bgcolor="#13131b",
            border_radius=15,
            padding=18,
            expand=True
        )

    # =========================
    # TELA DASHBOARD
    # =========================

    def tela_dashboard():

        atualizar_stats()

        status = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "STATUS DA PERSONAGEM",
                            size=12,
                            color="#9999a8",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Container(
                            expand=True
                        ),

                        nivel_text
                    ]
                ),

                ft.Divider(
                    color="#292934"
                ),

                ft.Row(
                    [
                        ft.Text(
                            "📍",
                            size=20
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "LOCALIZAÇÃO",
                                    size=10,
                                    color="#777784"
                                ),

                                localizacao_text
                            ],
                            spacing=2
                        )
                    ]
                ),

                ft.Row(
                    [
                        ft.Text(
                            "🚘",
                            size=20
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "VEÍCULO",
                                    size=10,
                                    color="#777784"
                                ),

                                veiculo_text
                            ],
                            spacing=2
                        )
                    ]
                ),

                ft.Row(
                    [
                        ft.Text(
                            "⛽",
                            size=20
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "COMBUSTÍVEL",
                                    size=10,
                                    color="#777784"
                                ),

                                combustivel_text
                            ],
                            spacing=2
                        )
                    ]
                ),

                ft.Row(
                    [
                        ft.ElevatedButton(
                            "ATUALIZAR LIVE",
                            on_click=atualizar_live
                        ),

                        ft.OutlinedButton(
                            "DIRIGIR",
                            on_click=dirigir
                        )
                    ],

                    spacing=10
                )
            ],

            spacing=12
        )

        radio_resumo = ft.Column(
            [
                ft.Text(
                    "META CITY RADIO",
                    size=12,
                    color="#9999a8",
                    weight=ft.FontWeight.BOLD
                ),

                musica_text,

                status_radio_text,

                ft.ProgressBar(
                    value=0.64
                ),

                ft.Row(
                    [
                        ft.TextButton(
                            "⏮",
                            on_click=musica_anterior
                        ),

                        ft.TextButton(
                            "▶ / ⏸",
                            on_click=tocar_radio
                        ),

                        ft.TextButton(
                            "⏭",
                            on_click=proxima_musica
                        )
                    ],

                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],

            spacing=8
        )

        missao = ft.Container(
            bgcolor="#13131b",
            border_radius=15,
            padding=20,

            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                "MISSÃO ATUAL",
                                size=12,
                                color="#9999a8",
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Container(
                                expand=True
                            ),

                            ft.Text(
                                "RECOMPENSA",
                                size=11,
                                color="#777784"
                            ),

                            ft.Text(
                                "VARIÁVEL",
                                size=13,
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    ),

                    ft.Divider(
                        color="#292934"
                    ),

                    missao_dashboard_text,

                    ft.TextButton(
                        "GERAR NOVA MISSÃO",
                        on_click=gerar_nova_missao
                    )
                ],

                spacing=8
            )
        )

        conteudo.controls = [

            titulo_pagina,

            ft.Text(
                "Bem-vinda de volta, Yumi 👋",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                [
                    card_stat(
                        "ESPECTADORES",
                        espectadores_text,
                        "👁"
                    ),

                    card_stat(
                        "DINHEIRO",
                        saldo_text,
                        "💰"
                    ),

                    card_stat(
                        "REPUTAÇÃO",
                        reputacao_text,
                        "⭐"
                    )
                ],

                spacing=15
            ),

            ft.Row(
                [
                    ft.Container(
                        content=status,
                        bgcolor="#13131b",
                        border_radius=15,
                        padding=20,
                        expand=2
                    ),

                    ft.Container(
                        content=radio_resumo,
                        bgcolor="#13131b",
                        border_radius=15,
                        padding=20,
                        expand=1
                    )
                ],

                spacing=15
            ),

            missao
        ]

    # =========================
    # TELA PERSONAGEM
    # =========================

    def aumentar_reputacao():

        nonlocal reputacao

        reputacao = min(
            100,
            reputacao + 5
        )

        atualizar_stats()

        aviso(
            "⭐ Reputação aumentada!"
        )

    def tela_personagem():

        progresso = ft.ProgressBar(
            value=xp / 100
        )

        conteudo.controls = [

            ft.Text(
                "PERSONAGEM",
                size=13,
                color="#777784",
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                "Perfil de Yumi_Roux",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                [

                    ft.Container(
                        bgcolor="#13131b",
                        border_radius=15,
                        padding=25,
                        expand=1,

                        content=ft.Column(
                            [
                                ft.Text(
                                    "👤",
                                    size=55
                                ),

                                ft.Text(
                                    nome,
                                    size=24,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.Text(
                                    "Streamer • Meta City RP",
                                    color="#777784"
                                ),

                                ft.Divider(
                                    color="#292934"
                                ),

                                ft.Text(
                                    f"🏆 Nível {nivel}"
                                ),

                                ft.Text(
                                    f"⭐ Reputação {reputacao}%"
                                ),

                                ft.Text(
                                    f"📍 {localizacao}"
                                )
                            ],

                            spacing=12
                        )
                    ),

                    ft.Container(
                        bgcolor="#13131b",
                        border_radius=15,
                        padding=25,
                        expand=1,

                        content=ft.Column(
                            [
                                ft.Text(
                                    "PROGRESSO",
                                    size=12,
                                    color="#9999a8",
                                    weight=ft.FontWeight.BOLD
                                ),

                                nivel_text,

                                progresso,

                                xp_text,

                                ft.Divider(
                                    color="#292934"
                                ),

                                ft.ElevatedButton(
                                    "TREINAR +10 XP",
                                    on_click=lambda e: (
                                        ganhar_xp(10),
                                        mostrar_tela(
                                            "Personagem"
                                        )
                                    )
                                ),

                                ft.OutlinedButton(
                                    "AUMENTAR REPUTAÇÃO",
                                    on_click=lambda e: (
                                        aumentar_reputacao(),
                                        mostrar_tela(
                                            "Personagem"
                                        )
                                    )
                                )
                            ],

                            spacing=12
                        )
                    )
                ],

                spacing=15
            )
        ]

    # =========================
    # TELA VEÍCULOS
    # =========================

    def tela_veiculos():

        cards = []

        for carro in veiculos:

            selecionado = (
                carro["nome"] == veiculo
            )

            cards.append(

                ft.Container(
                    bgcolor="#13131b",
                    border_radius=15,
                    padding=20,
                    expand=True,

                    content=ft.Column(
                        [
                            ft.Text(
                                "🚘",
                                size=40
                            ),

                            ft.Text(
                                carro["nome"],
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                carro["tipo"],
                                size=12,
                                color="#777784"
                            ),

                            ft.Text(
                                f"⛽ Combustível: "
                                f"{carro['combustivel']}%"
                            ),

                            ft.ProgressBar(
                                value=(
                                    carro["combustivel"]
                                    / 100
                                )
                            ),

                            ft.ElevatedButton(
                                "SELECIONADO"
                                if selecionado
                                else "USAR VEÍCULO",

                                on_click=lambda e,
                                n=carro["nome"]:
                                trocar_veiculo(n)
                            )
                        ],

                        spacing=10
                    )
                )
            )

        conteudo.controls = [

            ft.Text(
                "VEÍCULOS",
                size=13,
                color="#777784",
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                "Garagem da Yumi",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                cards,
                spacing=15
            ),

            ft.Container(
                bgcolor="#13131b",
                border_radius=15,
                padding=20,

                content=ft.Column(
                    [
                        ft.Text(
                            f"🚘 Veículo atual: {veiculo}",
                            size=17,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            f"⛽ Combustível: "
                            f"{combustivel}%",
                            color="#9999a8"
                        ),

                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "ABASTECER",
                                    on_click=abastecer
                                ),

                                ft.OutlinedButton(
                                    "DIRIGIR",
                                    on_click=dirigir
                                )
                            ],

                            spacing=10
                        )
                    ],

                    spacing=10
                )
            )
        ]

    # =========================
    # TELA MISSÕES
    # =========================

    def tela_missoes():

        lista = []

        for i, missao in enumerate(
            missoes
        ):

            if missao["status"] == "Disponível":

                acao = ft.ElevatedButton(
                    "ACEITAR",

                    on_click=lambda e,
                    indice=i:
                    aceitar_missao(indice)
                )

            elif missao["status"] == "Em andamento":

                acao = ft.ElevatedButton(
                    "CONCLUIR",

                    on_click=lambda e,
                    indice=i:
                    concluir_missao(indice)
                )

            else:

                acao = ft.OutlinedButton(
                    "CONCLUÍDA",
                    disabled=True
                )

            lista.append(

                ft.Container(
                    bgcolor="#13131b",
                    border_radius=15,
                    padding=20,

                    content=ft.Row(
                        [
                            ft.Text(
                                missao["icone"],
                                size=35
                            ),

                            ft.Column(
                                [
                                    ft.Text(
                                        missao["nome"],
                                        size=16,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    ft.Text(
                                        f"💰 R$ "
                                        f"{missao['recompensa']} "
                                        f" • ⭐ "
                                        f"{missao['xp']} XP",

                                        size=12,
                                        color="#9999a8"
                                    ),

                                    ft.Text(
                                        missao["status"],
                                        size=12,
                                        color="#ff3b81"
                                    )
                                ],

                                expand=True,
                                spacing=5
                            ),

                            acao
                        ],

                        spacing=15
                    )
                )
            )

        conteudo.controls = [

            ft.Text(
                "MISSÕES",
                size=13,
                color="#777784",
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                "Trabalhos de Meta City",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            *lista
        ]

    # =========================
    # TELA INVENTÁRIO
    # =========================

    def tela_inventario():

        lista = []

        for i, item in enumerate(
            inventario
        ):

            lista.append(

                ft.Container(
                    bgcolor="#13131b",
                    border_radius=15,
                    padding=18,

                    content=ft.Row(
                        [
                            ft.Text(
                                item[1],
                                size=30
                            ),

                            ft.Column(
                                [
                                    ft.Text(
                                        item[0],
                                        size=16,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    ft.Text(
                                        f"Quantidade: "
                                        f"{item[2]}",
                                        size=12,
                                        color="#9999a8"
                                    )
                                ],

                                expand=True
                            ),

                            ft.ElevatedButton(
                                "USAR",

                                on_click=lambda e,
                                indice=i:
                                usar_item(indice)
                            )
                        ],

                        spacing=15
                    )
                )
            )

        conteudo.controls = [

            ft.Text(
                "INVENTÁRIO",
                size=13,
                color="#777784",
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                "Mochila da Yumi",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            *lista,

            ft.Container(
                bgcolor="#13131b",
                border_radius=15,
                padding=18,

                content=ft.Row(
                    [
                        ft.Text(
                            "ADICIONAR ITEM:",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.TextButton(
                            "📱 Celular",

                            on_click=lambda e:
                            adicionar_item(
                                "Celular",
                                "📱"
                            )
                        ),

                        ft.TextButton(
                            "🩹 Kit médico",

                            on_click=lambda e:
                            adicionar_item(
                                "Kit médico",
                                "🩹"
                            )
                        ),

                        ft.TextButton(
                            "📻 Rádio",

                            on_click=lambda e:
                            adicionar_item(
                                "Rádio",
                                "📻"
                            )
                        )
                    ],

                    wrap=True
                )
            )
        ]

    # =========================
    # TELA RÁDIO
    # =========================

    def tela_radio():

        conteudo.controls = [

            ft.Text(
                "RÁDIO",
                size=13,
                color="#777784",
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                "Meta City Radio",
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            ft.Container(
                bgcolor="#13131b",
                border_radius=20,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text(
                            "📻",
                            size=65
                        ),

                        musica_text,

                        ft.Text(
                            "Yumi_Roux FM",
                            size=13,
                            color="#777784"
                        ),

                        status_radio_text,

                        ft.ProgressBar(
                            value=0.64
                        ),

                        ft.Row(
                            [
                                ft.TextButton(
                                    "⏮ ANTERIOR",
                                    on_click=musica_anterior
                                ),

                                ft.TextButton(
                                    "▶ / ⏸",
                                    on_click=tocar_radio
                                ),

                                ft.TextButton(
                                    "PRÓXIMA ⏭",
                                    on_click=proxima_musica
                                )
                            ],

                            alignment=(
                                ft.MainAxisAlignment.CENTER
                            )
                        ),

                        ft.Divider(
                            color="#292934"
                        ),

                        volume_text,

                        ft.Row(
                            [
                                ft.OutlinedButton(
                                    "− VOLUME",
                                    on_click=diminuir_volume
                                ),

                                ft.ElevatedButton(
                                    "+ VOLUME",
                                    on_click=aumentar_volume
                                )
                            ],

                            alignment=(
                                ft.MainAxisAlignment.CENTER
                            )
                        )
                    ],

                    horizontal_alignment=(
                        ft.CrossAxisAlignment.CENTER
                    ),

                    spacing=15
                )
            )
        ]

    # =========================
    # NAVEGAÇÃO
    # =========================

    def mostrar_tela(nome_tela):

        titulo_pagina.value = (
            nome_tela.upper()
        )

        if nome_tela == "Dashboard":

            tela_dashboard()

        elif nome_tela == "Personagem":

            tela_personagem()

        elif nome_tela == "Veículos":

            tela_veiculos()

        elif nome_tela == "Missões":

            tela_missoes()

        elif nome_tela == "Inventário":

            tela_inventario()

        elif nome_tela == "Rádio":

            tela_radio()

        page.update()

    # =========================
    # BOTÕES DO MENU
    # =========================

    def botao_menu(
        texto,
        icone
    ):

        return ft.TextButton(

            content=ft.Row(
                [
                    ft.Text(
                        icone,
                        size=18
                    ),

                    ft.Text(
                        texto,
                        size=14,
                        weight=ft.FontWeight.BOLD
                    )
                ],

                spacing=12
            ),

            on_click=lambda e,
            nome_menu=texto:
            mostrar_tela(nome_menu)
        )

    # =========================
    # SIDEBAR
    # =========================

    sidebar = ft.Container(

        width=210,

        bgcolor="#101017",

        padding=20,

        content=ft.Column(
            [
                ft.Text(
                    "META",
                    size=28,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "CITY",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#ff3b81"
                ),

                ft.Divider(
                    color="#292934"
                ),

                botao_menu(
                    "Dashboard",
                    "⌂"
                ),

                botao_menu(
                    "Personagem",
                    "👤"
                ),

                botao_menu(
                    "Veículos",
                    "🚗"
                ),

                botao_menu(
                    "Missões",
                    "🎯"
                ),

                botao_menu(
                    "Inventário",
                    "🎒"
                ),

                botao_menu(
                    "Rádio",
                    "📻"
                ),

                ft.Container(
                    expand=True
                ),

                ft.Text(
                    "STREAMER",
                    size=10,
                    color="#777784"
                ),

                ft.Text(
                    nome,
                    size=15,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "META CITY RP",
                    size=11,
                    color="#777784"
                )
            ],

            spacing=8
        )
    )

    # =========================
    # HEADER
    # =========================

    header = ft.Container(

        height=70,

        padding=25,

        bgcolor="#101017",

        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Yumi_Roux",
                            size=21,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            "Meta City Roleplay",
                            size=11,
                            color="#777784"
                        )
                    ],

                    spacing=2
                ),

                ft.Container(
                    expand=True
                ),

                ft.Container(
                    bgcolor="#24111b",
                    border_radius=20,
                    padding=15,

                    content=ft.Row(
                        [
                            ft.Text(
                                "●",
                                color="#ff3b81",
                                size=12
                            ),

                            ft.Text(
                                "AO VIVO",
                                size=12,
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                ),

                ft.Text(
                    "META CITY",
                    size=13
                )
            ],

            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    # =========================
    # CHAT
    # =========================

    chat_panel = ft.Container(

        width=285,

        bgcolor="#101017",

        padding=18,

        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "CHAT DA LIVE",
                            size=13,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Container(
                            expand=True
                        ),

                        ft.Text(
                            "1.247 online",
                            size=10,
                            color="#777784"
                        )
                    ]
                ),

                ft.Divider(
                    color="#292934"
                ),

                chat,

                ft.Row(
                    [
                        mensagem_input,

                        ft.TextButton(
                            "➤",
                            on_click=enviar_mensagem
                        )
                    ]
                )
            ],

            expand=True
        )
    )

    # =========================
    # LAYOUT
    # =========================

    page.add(

        ft.Row(
            [
                sidebar,

                ft.Column(
                    [
                        header,

                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Container(
                                        content=conteudo,
                                        padding=25,
                                        expand=True
                                    ),

                                    chat_panel
                                ],

                                expand=True
                            ),

                            expand=True
                        )
                    ],

                    spacing=0,
                    expand=True
                )
            ],

            spacing=0,
            expand=True
        )
    )

    # =========================
    # INICIAR NO DASHBOARD
    # =========================

    mostrar_tela("Dashboard")


# =========================
# EXECUTAR
# =========================

ft.app(target=main) 