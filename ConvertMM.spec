<<<<<<< HEAD
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ConvertMM.py'],
             pathex=['C:\\JonRob\\REPO\\GimmeInches'],
             binaries=[],
             datas=[('mmicon.ICO','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Gimme Inches v3.2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\JonRob\\REPO\\GimmeInches\\mmicon.ICO')
=======
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ConvertMM.py'],
             pathex=['C:\\JonRob\\REPO\\GimmeInches'],
             binaries=[],
             datas=[('mmicon.ICO','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Gimme Inches v3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\JonRob\\REPO\\GimmeInches\\mmicon.ICO')
>>>>>>> 1bda16814c81dcc21fcb2be16797f231b787264e
