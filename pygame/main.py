import pygame

#$ Init
pygame.init()
#? Variable running game
isRun = True

#* membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

#* Object game
#& Posisi
x = 250
y = 250

#& Ukuran
panjang = 20
lebar = 20

#& Kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)
    
    #$ User input, Database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    #* Mengambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    #& Ambil kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < window_panjang -panjang:
        y += speed
    
    
    #$ Update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(250,120,0),(x,y,panjang,lebar))
    #$ Render ke display
    pygame.display.update()
pygame.quit()