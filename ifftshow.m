function [  ] = ifftshow( f )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
ft = abs(f);
fm = max(ft(:));
imshow(ft/fm)

end

