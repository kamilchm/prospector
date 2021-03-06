import os
import re
from prospector.formatters.base import Formatter


class PylintFormatter(Formatter):
    """
    This formatter outputs messages in the same way as pylint -f parseable , which is used by several
    tools to parse pylint output. This formatter is therefore a compatability shim between tools built
    on top of pylint and prospector itself.
    """

    def render(self, summary=True, messages=True):
        # this formatter will always ignore the summary
        cur_loc = None
        output = []
        for message in sorted(self.messages):
            if cur_loc != message.location.path:
                cur_loc = message.location.path
                module_name = message.location.path.replace(os.path.sep, '.')
                module_name = re.sub(r'(\.__init__)?\.py$', '', module_name)

                header = '************* Module %s' % module_name
                output.append(header)

            #   ={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}
            # prospector/config.py:65: [C0111(missing-docstring), build_default_sources] Missing function docstring

            template = '%(path)s:%(line)s: [%(source)s:%(code)s(), %(function)s] %(message)s'
            output.append(template % {
                'path': message.location.path,
                'line': message.location.line,
                'source': message.source,
                'code': message.code,
                'function': message.location.function,
                'message': message.message.strip()
            })

        return '\n'.join(output)