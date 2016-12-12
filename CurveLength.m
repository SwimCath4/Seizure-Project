function feat = CurveLength(X) 
feat = sum(X(2:end,:) - X(1:end-1,:));
end