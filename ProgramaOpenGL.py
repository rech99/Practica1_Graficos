from OpenGL.GL import *
from glew_wish import *
import glfw 
import random

def main():
    #inicia glfw
    if not glfw.init():
        return
    window = glfw.create_window(800,600, "Mi Vnetana", None, None)


    #configuramos OpenGL
    glfw.window_hint(glfw. SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return

    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validacion de las funciones modernas de OpenGL
    glewExperimental = True

    if glewInit() != GLEW_OK:
        print ("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        
        color_1= random.random()
        color_2= random.random()
        color_3= random.random()
       
        #Color
        glViewport(0,0,800,600)
        
        
        #Color de borrado
        glClearColor(color_1,color_2,color_3,1)
        

        #Borra contenido de a ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       


        #Dibujar

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar meoria
    glfw.destroy_window(window)
    #Termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()

