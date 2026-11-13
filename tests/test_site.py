from pathlib import Path
from html.parser import HTMLParser
import unittest
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.inputs=[]; self.buttons=[]
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag); a=dict(attrs)
        if tag=='input': self.inputs.append(a)
        if tag=='button': self.buttons.append(a)
class SiteTests(unittest.TestCase):
    def test_contact_form_structure(self):
        p=Parser(); p.feed(Path('index.html').read_text(encoding='utf-8'))
        self.assertIn('h1',p.tags); self.assertIn('form',p.tags)
        self.assertTrue(any(a.get('name')=='name' and 'required' in a for a in p.inputs))
        self.assertTrue(any(a.get('name')=='email' and a.get('type')=='email' and 'required' in a for a in p.inputs))
        self.assertTrue(any(a.get('type')=='submit' for a in p.buttons))
if __name__=='__main__': unittest.main()
