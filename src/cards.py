# -*- coding: utf-8 -*-

import urwid
from picmagic import read as picRead
from tools import validate_uri
from widgets import *
from testers import *

class Cards(object):
  credentials = []

  def __init__(self, app):
    self.app = app

  def welcome(self):
    pic = picRead('rsc/welcome.bmp', align='right')
    text = urwid.Text((
        'text',
        '%s is a CLI tool for auditing MongoDB servers, detecting poor security settings and performing automated penetration testing.'
        % self.app.name))
    button = urwid.AttrMap(
        TextButton(
            'Start', on_press=self.choose_test), 'button')
    card = Card(text, header=pic, footer=button)
    self.app.render(card)

  def choose_test(self, button=None):
    txt = urwid.Text([('text bold', self.app.name),
        ' provides two distinct types of test suites covering  security in different depth. Please choose which tests you want to run:'])

    basic = ImageButton(
        picRead('rsc/%s' % 'bars_min.bmp'),
        [('text bold', 'Basic'),
         ('text', 'Analize server perimeter security. (Does not require valid credentials)')])
    advanced = ImageButton(
        picRead('rsc/%s' % 'bars_max.bmp'),
        [('text bold', 'Advanced'),
         ('text', 'Connect to MongoDB server and analize security from inside. (Requires valid credentials)')])
    content = urwid.Pile([txt, div, basic, advanced])
    urwid.connect_signal(basic, 'click', self.basic_test)
    urwid.connect_signal(advanced, 'click', self.advanced_test)
    card = Card(content)
    self.app.render(card)

  def basic_test(self, _):
    intro = urwid.Pile([
      urwid.Text(('text bold', 'Basic test')),
      div,
      urwid.Text(['Please provide the URI of your MongoDB server (',('text italic', 'domain.tld:port'), ')'])
    ])
    validate = lambda form, uri: validate_uri(uri, form, "Invalid URI", self.run_basic)
    form = FormCard(intro, ['URI'], 'Run basic test', validate, back=self.choose_test)
    self.app.render(form)

  def advanced_test(self, _):
    intro = urwid.Pile([
      urwid.Text(('text bold', 'Advanced test')),
      div,
      urwid.Text(['Please enter your MongoDB URI (', ('text italic', 'mongodb://user:password@domain.tld:port/database'), ')'])
    ])
    validate = lambda form, mongodb_uri: validate_uri(mongodb_uri, form, "Invalid MongoDB URI", self.run_advanced)
    self.app.render(FormCard(intro,["MongoDB URI"], "Run advanced test", validate, back=self.choose_test))

  #TODO run basic and advanced are almost identical, refactor
  def run_basic(self, cred):
    title = 'Basic'
    test_runner = TestRunner(title, cred, tests, self.app, self.display_results)
    pic = picRead('rsc/check_basic.bmp', align='right')

    footer = urwid.AttrMap(TextButton('Cancel', align='left', on_press=self.choose_test),'button')
    card = Card(test_runner, header=pic, footer=footer)
    self.app.render(card)
    test_runner.run()


  def run_advanced(self, cred):
    title = 'Advanced'
    test_runner = TestRunner(title, cred, tests, self.app, self.display_results)
    pic = picRead('rsc/check_advanced.bmp', align='right')

    footer = urwid.AttrMap(TextButton('Cancel', align='left', on_press=self.choose_test),'button')
    card = Card(test_runner, header=pic, footer=footer)
    self.app.render(card)
    test_runner.run()

  def display_results(self, title, list_walker, total):
    intro = urwid.Text(('text bold',title + ' test results'))
    footer = urwid.AttrMap(TextButton('Back', align='left', on_press=self.choose_test),'button')
    boxAdapter = urwid.BoxAdapter(urwid.ListBox(list_walker), height=12)
    pile = urwid.Pile([intro, div, boxAdapter, div, total])
    card = Card(pile, footer=footer)
    self.app.render(card)
