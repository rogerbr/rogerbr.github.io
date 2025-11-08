from mkdocs.plugins import BasePlugin

from pygments.lexers import get_lexer_by_name

def on_config(config, **kwargs):
    import lexer_gdscript.gdscript
    lexer = get_lexer_by_name("gdscript")
    print("✅ Active GDScript lexer:", lexer)
    return config

class CustomLexerPlugin(BasePlugin):
    def on_config(self, config):
        #import lexer_gdscript.gdscript_lexer
        #import lexer_gdscript.gdscript_style
        import lexer_gdscript.gdscript
        print("✅ MkDocs Official GDScript lexer plugin loaded.")
        return config