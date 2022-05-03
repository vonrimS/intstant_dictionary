import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view='hHh lpR fFf')
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model='Left', bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes='fit')

        qList = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.Br(a=qList)
        jp.Br(a=qList)
        jp.A(a=qList, text='Home', href='/', classes=a_classes)
        jp.Br(a=qList)
        jp.Br(a=qList)
        jp.A(a=qList, text='About', href='/about', classes=a_classes)
        jp.Br(a=qList)
        jp.Br(a=qList)
        jp.A(a=qList, text='Dictionary', href='/dictionary', classes=a_classes)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page!', classes='text-4xl m-2')
        jp.Div(a=div, text="""
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque quis euismod neque. Etiam quis est a sem dignissim dignissim sit amet non urna. Aliquam ut convallis quam. Aenean eu rutrum neque. Nullam facilisis lobortis lacus, eget accumsan mauris tincidunt non. Maecenas sit amet leo mi. Sed malesuada nisi id enim placerat, sit amet ullamcorper purus tincidunt. Nam elementum dictum lorem in tempus. Phasellus porta odio id quam facilisis varius. Phasellus lectus nisl, convallis et sem et, faucibus dictum dolor. Mauris lorem ante, vestibulum nec dictum vel, elementum sit amet nibh.
                    Pellentesque sollicitudin lacinia eros. Vestibulum vitae nisi odio. Sed accumsan eu erat non fringilla. Quisque at lorem purus. Donec justo purus, sodales vel mi vel, venenatis aliquet leo. Donec euismod erat nec ornare imperdiet. Nunc eleifend tempor arcu. Integer efficitur nibh et venenatis sollicitudin. Fusce porta nulla et tincidunt luctus. Duis ultricies, est sit amet tempus feugiat, ex enim commodo tellus, ac blandit lectus felis vitae urna. Quisque vitae fringilla nunc, sed pellentesque dui. Sed nec cursus orci. Donec ac cursus lacus.            
                    Donec tempor ante at ante pharetra, eu bibendum augue cursus. Pellentesque tincidunt quam sit amet eros pulvinar, eu finibus nisi posuere. Curabitur quis mauris sem. Proin et commodo lectus. Etiam vel mi enim. Nunc ac sapien lacinia, malesuada metus ut, tincidunt ipsum. Nullam pulvinar cursus sagittis. Suspendisse posuere turpis sed facilisis ullamcorper. Morbi sodales sem et sem vehicula, at viverra turpis consectetur. Donec placerat quam a tellus eleifend venenatis.
                """, classes='text-lg')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value == True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
