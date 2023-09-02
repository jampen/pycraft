import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(512, 512)
glutInitWindowPosition(0, 0)

window = glutCreateWindow('My Window')
glutDisplayFunc(render)
glutIdleFunc(render)
glutMainLoop()
