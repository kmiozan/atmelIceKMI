# -*- mode: python -*-

block_cipher = None


a = Analysis(['delta.py'],
             pathex=['D:\\Users\\26000595\\Desktop\\atmelIceKMI'],
             binaries=None,
             datas=[('atprogram_mono.bat', '.'), ('atprogram_monoftc.bat', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='delta',
          debug=False,
          strip=False,
          upx=True,
          console=True )
