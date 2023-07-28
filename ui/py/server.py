# Copyright 2023 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Frontend server for static angular files."""
import os

import flask
import flask_cors

app = flask.Flask(
    __name__,
    static_url_path='',
    static_folder='/var/www',
    template_folder='/var/www',
)
flask_cors.CORS(app)


@app.route('/')
def index():
  return flask.send_from_directory('/var/www', 'index.html')


@app.route('/favicon.ico')
def favicon():
  return flask.send_from_directory(
      '/var/www', 'favicon.ico', mimetype='image/vnd.microsoft.icon'
  )


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
