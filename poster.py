from requests import post
post('http://localhost:5000/api', data={'name': "сила",
                                        "definition": r'''\begin{equation*}
\vec{F} = \frac{d\vec{p}}{dt}
\end{equation*}''', 'section': 'механика'})

post('http://localhost:5000/api', data={'name': "путь",
                                        "definition": r'''\begin{equation*}
S = S_{0} + \upsilon_{0x}t
\end{equation*}''', 'section': 'равномерное прямолинейное движение'})

post('http://localhost:5000/api', data={'name': "путь",
                                        "definition": r'''\begin{equation*}
S = S_{0} + \upsilon_{0x}t + \frac{a_{x}t^{2}}{2}
\end{equation*}''', 'section': 'равноускоренное прямолинейное движение'})

post('http://localhost:5000/api', data={'name': "скорость",
                                        "definition": r'''\begin{equation*}
v = \upsilon_{0x} + a_{x}t
\end{equation*}''', 'section': 'равноускоренное прямолинейное движение'})

post('http://localhost:5000/api', data={'name': "ускорение",
                                        "definition": r'''\begin{equation*}
a_{цс} = \frac{\upsilon^{2}}{R} = /omega^{2}R
\end{equation*}''', 'section': 'движение по окружности'})

post('http://localhost:5000/api', data={'name': "скорость",
                                        "definition": r'''\begin{equation*}
\upsilon = \omegaR
\end{equation*}''', 'section': 'движение по окружности'})

post('http://localhost:5000/api', data={'name': "угловая скорость",
                                        "definition": r'''\begin{equation*}
\omega = 2\pi\upsilon = frac{2\pi}{T}
\end{equation*}''', 'section': 'движение по окружности'})

post('http://localhost:5000/api', data={'name': "плотность",
                                        "definition": r'''\begin{equation*}
\rho = \frac{m}{V}
\end{equation*}''', 'section': 'динамика'})

post('http://localhost:5000/api', data={'name': "сила",
                                        "definition": r'''\begin{equation*}
F = G\frac{m_{1}m_{2}}{R^{2}}
\end{equation*}''', 'section': 'динамика'})

post('http://localhost:5000/api', data={'name': "сила",
                                        "definition": r'''\begin{equation*}
F_{тяж} = \frac{GMm}{(R_{0} + h)^{2}}
\end{equation*}''', 'section': 'динамика'})