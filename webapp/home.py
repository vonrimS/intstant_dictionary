import justpy as jp


class Home:
    path = '/home'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page!', classes='text-4xl m-2')
        jp.Div(a=div, text="""
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque quis euismod neque. Etiam quis est a sem dignissim dignissim sit amet non urna. Aliquam ut convallis quam. Aenean eu rutrum neque. Nullam facilisis lobortis lacus, eget accumsan mauris tincidunt non. Maecenas sit amet leo mi. Sed malesuada nisi id enim placerat, sit amet ullamcorper purus tincidunt. Nam elementum dictum lorem in tempus. Phasellus porta odio id quam facilisis varius. Phasellus lectus nisl, convallis et sem et, faucibus dictum dolor. Mauris lorem ante, vestibulum nec dictum vel, elementum sit amet nibh.
                    Pellentesque sollicitudin lacinia eros. Vestibulum vitae nisi odio. Sed accumsan eu erat non fringilla. Quisque at lorem purus. Donec justo purus, sodales vel mi vel, venenatis aliquet leo. Donec euismod erat nec ornare imperdiet. Nunc eleifend tempor arcu. Integer efficitur nibh et venenatis sollicitudin. Fusce porta nulla et tincidunt luctus. Duis ultricies, est sit amet tempus feugiat, ex enim commodo tellus, ac blandit lectus felis vitae urna. Quisque vitae fringilla nunc, sed pellentesque dui. Sed nec cursus orci. Donec ac cursus lacus.            
                    Donec tempor ante at ante pharetra, eu bibendum augue cursus. Pellentesque tincidunt quam sit amet eros pulvinar, eu finibus nisi posuere. Curabitur quis mauris sem. Proin et commodo lectus. Etiam vel mi enim. Nunc ac sapien lacinia, malesuada metus ut, tincidunt ipsum. Nullam pulvinar cursus sagittis. Suspendisse posuere turpis sed facilisis ullamcorper. Morbi sodales sem et sem vehicula, at viverra turpis consectetur. Donec placerat quam a tellus eleifend venenatis.
                """, classes='text-lg')
        return wp


