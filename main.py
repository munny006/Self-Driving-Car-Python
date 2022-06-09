import pygame

pygame.init()
window = pygame.display.set_mode((1200,400))
track = pygame.image.load('track3.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(30,60))
car_x = 150
car_y = 300
cam_x_offset = 0
cam_y_offset = 0
focal_dist = 25
disrection = 'up'

drive = True
clock = pygame.time.Clock()


while drive:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    cam_x = car_x + cam_x_offset +15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x,cam_y - focal_dist))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]
    print(up_px,right_px,down_px)
    if disrection == 'up' and up_px != 255 and right_px == 255:
        disrection = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car,-90)
    elif disrection == 'right' and right_px !=255 and down_px == 255:
        disrection = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car =  pygame.transform.rotate(car,-90)
    elif disrection == 'down' and down_px != 255 and right_px == 255 :
        disrection = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car,90)
    elif  disrection == 'right' and right_px != 255 and up_px == 255:
        disrection = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car,90)
    if disrection == 'up' and up_px == 255:
    #if up_px == 255:
     car_y = car_y - 2
    elif disrection == 'right' and right_px == 255:
        car_x = car_x + 2
    elif disrection == 'down' and down_px == 255:
        car_y = car_y + 2
    window.blit(track, (0, 0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()
