function [ out ] = gaussian_hp( im,d )
%UNTITLED9 Summary of this function goes here
%   Detailed explanation goes here
[ht,wid] = size(im);
[x,y] = meshgrid(-floor(wid/2):floor((wid-1)/2),-floor(ht/2):floor((ht-1)/2));
out = 1 - exp(-(x.^2 + y.^2)./(2*d*d));
end

