function [] = fftshow( f )
%UNTITLED2 Summary of this function goes here
%   input is fft shifted
ft = log(1+abs(f));
fm = max(ft(:));
imshow(im2uint8(ft/fm))

end

