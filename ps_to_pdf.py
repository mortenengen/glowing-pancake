import subprocess

ps_to_convert = [
    'css_pt_t0.PS'
    ]

for this_ps in ps_to_convert:
    arguments = ['ps2pdf', this_ps]
    subprocess.run(arguments)