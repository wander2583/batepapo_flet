import flet as ft


def main(pagina):  # TODO: Adicionar a página como argumento
    titulo = ft.Text("Bate Papo ao Vivo.")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe("enviar_mensagem", enviar_mensagem_tunel)

    titulo_janela = ft.Text("Só Sei que foi assim...")
    campo_nome_usuario = ft.TextField(label="Usuário?")

    def enviar_mensagem(
        evento,
    ):  # FIX: Verificar como retirar o aviso de variável não utilizada
        texto = texto_mensagem.value
        texto = f"{campo_nome_usuario.value}: {texto}"
        chat.controls.append(ft.Text(texto))
        pagina.pubsub.send_all(texto)
        texto_mensagem.value = ""
        pagina.update()

    texto_mensagem = ft.TextField(
        label="Digite sua mensagem", on_submit=enviar_mensagem
    )
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column([])

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_no_chat(
        evento,
    ):  # FIX: Verificar como retirar o aviso de variável não utilizada
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)

        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        chat.controls.append(ft.Text(texto_entrou_chat))

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_no_chat)

    janela = ft.AlertDialog(
        title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main)
