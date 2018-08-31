cube = imread('images/cube.jpg');
red = cube(:,:,1);
green = cube(:,:,2);
blue = cube(:,:,3);
subplot(1,4,1)
imshow(cube)
title('original')
subplot(1,4,2)
imshow(red)
title('red')
subplot(1,4,3)
imshow(green)
title('green')
subplot(1,4,4)
imshow(blue)
title('blue')