import segno
import flet as ft
import base64
import io

def create_qr_str(content: str) -> str:
    """Create QR image string for updating ft.Image content"""
    qr = segno.make(content, error = 'h')
    buffer = io.BytesIO()
    qr.save(buffer, kind='png', scale = 8)
    return base64.b64encode(buffer.read()).decode('utf-8')

    # qr_img.save(buffer, format="PNG")
    # qr_code = "data:image/png;base64,"+base64.b64encode(buffer.getvalue()).decode("utf-8")


def read_image_str(path: str) -> str:
    """Return image string for updating ft.Image content"""
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def start(page: ft.Page):
    page.title = ('QR Generator')
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def gen_qr(qr: ft.Image):
        print("gen_qr start")
        # qr_content = content_input.value
        # qrcode = segno.make(qr_content, error='h')
        # qrcode.save('qrcode.png', scale=8)
        # qr.src_base64 = read_image_str("qrcode.png")
        qr.src_base64 = create_qr_str(content_input.value)
        qr.update()
        # qr = ft.Image(src="qrcode.png", scale=1)
        # qr_container.content = qr
        # qr_container = ft.Container(
        #     content=qr,
        #     alignment=ft.alignment.center
        # )
        #page.add(qr)
        #print(qr_content)
        page.update()
        print("updated")

    content_input = ft.TextField(hint_text="What needs to be in the qr code?", scale=1, width=720)
    #qr = ft.Image(src="qrcode.png", scale=1)
    # qr = ft.Image(src_base64=create_qr_str('random text'))
    qr = ft.Image(src_base64="iVBORw0KGgoAAAANSUhEUgAAABkAAAAgCAYAAADnnNMGAAAACXBIWXMAAAORAAADkQFnq8zdAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA6dJREFUSImllltoHFUYx3/fzOzm0lt23ZrQ1AQbtBehNpvQohgkBYVo410RwQctNE3Sh0IfiiBoIAjqi6TYrKnFy4O3oiiRavDJFi3mXomIBmOxNZe63ay52GR3Zj4f2sTEzmx3m//TYf7/c35zvgPnO6KqrESXqpq3muocAikv6m+/zytj3ejik1VN21G31YA9CgJ6xC+bMyQZPVCuarciPAMYC99V6Vw5pLbFSibHmlVoRVj9P3cmPBM8tSJI/M6mzabpfoAQ9fIF7WK4bd5vvuFnLGgy2vi0abg94A0AcJGvMq3hDxGRyar9r4F+iLAm0yIiRk8m37tctS1WsrIhhrI30+Srmg+J87OXUf3lWGS1q89dC6ltsSanxk4Aj2QBABii96300g87P/rtlrWr8l+vyDMfdlXSyyEikqxsiOUAQJCBhfHdXRfCq1LSsSlcWG+KBAGStvvrMkgiuv8lUc2mREukPwLUfHG+uTQv8Eown7VL3XlbBxYhf1c17hbVF3MDwA9bts280TnaU1YYqPby07aeFlUlHt27wSQ4CLo+F8AvoTCvHmyKF+ZbEb/M77P2LgvAwmrTHAHflN3KZxVbMC2jMFNOpgPnrMSOhvvFkMezXdwV4ePbtvHtxnJAMQ0j4JtVnO+eLb5oiSlt5HDbv7t1O90lpYCCCKbhfzW5kAIwUAazR0BlfII8Ow0I6uoVmI9MyAMwbMs8CExmDbk4zgu931MyO4OI4KrYflkRjOoTI+uM9d1vjotwKPu9QMk/sxzuO8POiVFcdZ1M2YBVsMEAKOqLvaPIe7mACuw0z/80SMH58SMplxlfiDhVi7dw2pltRhjKBQTQdrSja2KKTfE551NHuaZ0QVPvWYQUn31/Vm2nDvgjF4grVJx6suSvrvrSJ/6cSW2Oz9mf264uNrB806xZ1k/CZ49dUKgDEtlCROX2hfHpx8pGuuo3PpqYulw8fjndOp1yhgtNKRevJ1FyR2Ola+jXAjdnwTkZ6o896GdWdxDw7IxFg+0DpmXchTKSBWQnIuJn9u4j7dt+13UfHXEkXQOcuQ4kMhVtqsgUyPiQiPQfHw1NB2sRjmXKuTg1NwwBYLhtPtQX26eqTwGXPDOqvmcC4Hnwfrrad94GrVsOYTqUTkQY+iTlNe/6O1miSP/x0VB/+wMIDwHn/vtV1iQC4Xv95uUEWVCoL9Y5Z+gdovoyMHUFJHv88jmVy0vTuw7cZNv2YaA61Bfb7ZX5F8SaUv2xwZevAAAAAElFTkSuQmCC")
    # qr_container = ''
    qr_container = ft.Container(
        content=qr,
        alignment=ft.alignment.center
    )
    gen_btn = ft.FilledTonalButton(text="Generate QR Code", on_click=lambda _: gen_qr(qr), width=200, height=50)
    #content.on_change = lambda text: print(content.value)

    page.add(
        ft.Column([ #Base
            ft.Container( #For content_input
                content=content_input,
                alignment=ft.alignment.Alignment(0,0)
            ),
            ft.Row([ #Another base for qr and gen_btn
                qr_container,
                ft.Container(
                    content=gen_btn,
                    padding=50,
                    alignment=ft.alignment.center
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
            )
        ],
            alignment=ft.alignment.center,
            spacing=50
        )
    )

if __name__ == "__main__":
    ft.app(port=1313, target=start)# view=ft.AppView.WEB_BROWSER)