function [ out ] = butterhp( im,d,n )
%UNTITLED5 Summary of this function goes here
%   im=image, d=cutoff frequency, n=order
[ht,col] = size(im);
[x,y] = meshgrid(-floor(col/2):floor((col-1)/2),-floor(ht/2):floor((ht-1)/2));
out = 1./(1+ d./(x.^2 + y.^2).^(2*n));

end

