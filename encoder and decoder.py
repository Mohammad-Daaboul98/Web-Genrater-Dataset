class ContextEncoder(nn.Module):

    def __init__(self):
        super(ContextEncoder, self).__init__()
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer=nn.TransformerEncoderLayer(d_model=142, nhead=8, dim_feedforward=128, dropout=0.1),
            num_layers=2)
    
    def forward(self, x):
        # x -> [-1, seq_size, 19]
        x, _ = self.transformer_encoder(x)
        return x

class Decoder(nn.Module):

    def __init__(self):
        super(Decoder, self).__init__()
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer=nn.TransformerDecoderLayer(d_model=1024+128, nhead=8, dim_feedforward=512, dropout=0.1),
            num_layers=2)
        self.l1 = nn.Linear(1024+128, 142)
    
    def forward(self, image_feature, context_feature, on_cuda = False):
        # image_feature -> [-1, 1024], context_feature -> [-1, seq_size=48, 128]
        image_feature = image_feature.unsqueeze(1)
        # image_feature -> [-1, 1, 1024]
        image_feature = image_feature.repeat(1, context_feature.size(1), 1)
        # image_feature -> [-1, seq_size, 1024]
        x = torch.cat((image_feature, context_feature), 2)
        # x -> [-1, seq_size=48, 1024+128]

        x, _ = self.transformer_decoder(x, context_feature)
        x = self.l1(x)
        # x = F.softmax(x, dim=1)
        return x
