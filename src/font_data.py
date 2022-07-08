from pyglet import resource

resource.path.append('res')

highlighted_font_image = resource.image('font.png')
Outlined = {
    "A" : [highlighted_font_image.get_region(0, 0, 25,25), 0, 0],
    "B" : [highlighted_font_image.get_region(25, 0, 25,25), 0, 0],
    "C" : [highlighted_font_image.get_region(50, 0, 25,25), 0, 0],
    "D" : [highlighted_font_image.get_region(75, 0, 25,25), 0, 0],
    "E" : [highlighted_font_image.get_region(99, 0, 26,25), 0, 0],
    "F" : [highlighted_font_image.get_region(125, 0, 25,25), 0, 0],
    "G" : [highlighted_font_image.get_region(150, 0, 25,25), 0, 0],
    "H" : [highlighted_font_image.get_region(175, 0, 25,25), 0, 0],
    "I" : [highlighted_font_image.get_region(206, 0, 12,25), 0, 0],
    "J" : [highlighted_font_image.get_region(225, 0, 25,25), 0, 0],
    "K" : [highlighted_font_image.get_region(250, 0, 25,25), 0, 0],
    "L" : [highlighted_font_image.get_region(275, 0, 22,25), 0, 0],
    "M" : [highlighted_font_image.get_region(300, 0, 25,25), 0, 0],
    "N" : [highlighted_font_image.get_region(325, 0, 25,25), 0, 0],
    "O" : [highlighted_font_image.get_region(349, 0, 27,26), 0, 0],
    "P" : [highlighted_font_image.get_region(375, 0, 25,25), 0, 0],
    "Q" : [highlighted_font_image.get_region(400, 0, 25,25), 0, 0],
    "R" : [highlighted_font_image.get_region(425, 0, 25,25), 0, 0],
    "S" : [highlighted_font_image.get_region(450, 0, 25,25), 0, 0],
    "T" : [highlighted_font_image.get_region(475, 0, 25,25), 0, 0],
    "U" : [highlighted_font_image.get_region(500, 0, 25,25), 0, 0],
    "V" : [highlighted_font_image.get_region(525, 0, 25,25), 0, 0],
    "W" : [highlighted_font_image.get_region(550, 0, 37,25), 0, 0],
    "X" : [highlighted_font_image.get_region(587, 0, 25,25), 0, 0],
    "Y" : [highlighted_font_image.get_region(614, 0, 23,25), 0, 0],
    "Z" : [highlighted_font_image.get_region(636, 0, 25,25), 0, 0],
    " " : [highlighted_font_image.get_region(660, 0, 15,25), 0, 0],
    
    #Lower-case
    "a" : [highlighted_font_image.get_region(2, 36, 17,25), 0, -1],
    "b" : [highlighted_font_image.get_region(27, 35, 19,28), 0, -3],
    "c" : [highlighted_font_image.get_region(53, 36, 17,25), 0, -1],
    "d" : [highlighted_font_image.get_region(77, 36, 19, 33), 0, -2],
    "e" : [highlighted_font_image.get_region(103, 36, 19, 33), 0, -1],
    "f" : [highlighted_font_image.get_region(130, 36, 14, 33), 0, -2],
    "g" : [highlighted_font_image.get_region(152, 32, 19, 39), 0, -4],
    "h" : [highlighted_font_image.get_region(177, 34, 18, 39), 0, -2],
    "i" : [highlighted_font_image.get_region(207, 32, 10, 39), 0, -3],
    "j" : [highlighted_font_image.get_region(231, 30, 9, 39), 0, -4],
    "k" : [highlighted_font_image.get_region(248, 33, 20, 34), 0, -3],
    "l" : [highlighted_font_image.get_region(284, 33, 7, 34), 0, -3],
    "m" : [highlighted_font_image.get_region(298, 33, 28, 24), 0, -2],
    "n" : [highlighted_font_image.get_region(328, 33, 18, 34), 0, -3],
    "o" : [highlighted_font_image.get_region(352, 33, 20, 34), 0, -3],
    "p" : [highlighted_font_image.get_region(376, 30, 19, 39), 0, -6],
    "q" : [highlighted_font_image.get_region(400, 30, 19, 39), 0, -6],
    "r" : [highlighted_font_image.get_region(429, 34, 12, 35), 0, -1],
    "s" : [highlighted_font_image.get_region(453, 34, 16, 35), 0, -1],
    "t" : [highlighted_font_image.get_region(479, 34, 16, 35), 0, -1],
    "u" : [highlighted_font_image.get_region(504, 34, 16, 35), 0, -1],
    "v" : [highlighted_font_image.get_region(527, 34, 18, 35), 0, -1],
    "w" : [highlighted_font_image.get_region(555, 34, 28, 35), 0, -1],
    "x" : [highlighted_font_image.get_region(591, 34, 18, 35), 0, -1],
    "y" : [highlighted_font_image.get_region(617, 30, 19, 39), 0, -7],
    "z" : [highlighted_font_image.get_region(642, 30, 18, 34), 0, -4.5],
    
    #Numbers
    "0" : [highlighted_font_image.get_region(4, 76, 21, 34), 0, -0.5],
    "1" : [highlighted_font_image.get_region(33, 76, 18, 35), 0, -0.5],
    "2" : [highlighted_font_image.get_region(59, 76, 19, 35), 0, -0.5],
    "3" : [highlighted_font_image.get_region(86, 76, 19, 35), 0, -0.5],
    "4" : [highlighted_font_image.get_region(112, 76, 21, 35), 0, -0.5],
    "5" : [highlighted_font_image.get_region(140, 76, 19, 35), 0, -0.5],
    "6" : [highlighted_font_image.get_region(167, 76, 19, 35), 0, -0.5],
    "7" : [highlighted_font_image.get_region(194, 76, 19, 35), 0, -0.5],
    "8" : [highlighted_font_image.get_region(220, 76, 20, 35), 0, -0.5],
    "9" : [highlighted_font_image.get_region(255, 76, 19, 35), 0, -0.5],
    
    #Special
    ":" : [highlighted_font_image.get_region(284, 76, 8, 35), 0, -0.5],
    "," : [highlighted_font_image.get_region(300, 70, 11, 35), -1, -5],
    "'" : [highlighted_font_image.get_region(354, 76, 6, 35), 0, -0.5],
    r'"' : [highlighted_font_image.get_region(370, 76, 12, 35), 0, -0.5],
    "." : [highlighted_font_image.get_region(319, 76, 8, 32), 0, -0.5],
    "?" : [highlighted_font_image.get_region(7, 112, 16, 32), 0, -0.5],
    "!" : [highlighted_font_image.get_region(35, 112, 8, 32), 0, -0.5],
}