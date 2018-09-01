function [ y ] = ada_thres( x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
if std2(x) < 1
    y = ones(size(x,1),size(x,2));
else
    y = im2bw(x,graythresh(x));
end
end

