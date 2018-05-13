# -*- encoding: utf-8 -*-

import os

from flask_cors import CORS

from app import create_app
# from flask_script import Manager, Shell
# from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
CORS(app, supports_credentials=True) #跨域解决
# manager = Manager(app)
# migrate = Migrate(app, db)
#
# def make_shell_context():
#     return dict(app=app, db=db)
#
# manager.add_command("shell",Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()