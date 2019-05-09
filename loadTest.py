import loading
kv_str = """
<LOAD>:
    size_hint: (None, None)
    height: 200
    width: 200
    max: 80
"""
def build(self):
    container = Builder.load_string(kv_str)
    Clock.schedule_interval(self.animate, 0.1)
    return container

loading.Main().run()