function [ out ] = gaussian_lp( im,d )
%UNTITLED8 Summary of this function goes here
%   Detailed explanation goes here
[ht,wid] = size(im);
[x,y] = meshgrid(-floor(wid/2):floor((wid-1)/2),-floor(ht/2):floor((ht-1)/2));
out = exp(-(x.^2 + y.^2)./(2*d*d));

end

