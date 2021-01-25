from distutils.core import setup
setup(
  name = 'GTCreator',         # How you named your package folder (MyLib)
  packages = ['GTCreator'],   # Chose the same as "name"
  version = '0.9',      # Start with a small number and increase it with every change you make
  license='apache-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Create your own timelapse from images simply',   # Give a short description about your library
  author = 'ecmgs',                   # Type in your name
  author_email = 'prog.ecmgs@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ECMGS/GTCreator/tree/main',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ECMGS/GTCreator/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['timelapse', 'ffmpeg', 'mp4'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'ffmpeg-python'
      ],
  entry_points={
      "console_scripts": ["GTCreator = GTCreator.GTCreator:__main__"]
    }
)
