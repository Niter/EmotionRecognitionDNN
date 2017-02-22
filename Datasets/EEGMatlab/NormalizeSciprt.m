% LoadData
WholeX = load('CWTX.mat');
WholeX = WholeX.WholeX;

% Normalization
WholeX_Normalized = zeros(1280, 63, 32, 32);

for i = 1:32;
    for j = 1:32;
        WholeX_Normalized(:, :, i, j) = Normalize(WholeX(:, :, i, j));
    end
end

fprintf('Start Store the Transformed Data\n');
save 'CWTX_Normalized.mat' WholeX_Normalized;
