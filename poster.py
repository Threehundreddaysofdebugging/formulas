from requests import post
print(post('http://localhost:5000/api', data={'name': "скорость",
                                              "definition": r'''\begin{equation*}
v = \frac{S}{t}
\end{equation*}''', 'section': 'механика'}).json())