class ContextEncoder(nn.Module):

    def __init__(self):
        super(ContextEncoder, self).__init__()
        self.rnn = nn.RNN(input_size=142, hidden_size=128, num_layers=2, batch_first=True)
    
    def forward(self, x, h=None):
        # x -> [-1, seq_size, 19], h -> [num_layer=2,-1, 128]

        if not h:
            h = torch.zeros((2, x.size(0), 128)).cuda()

        x, _ = self.rnn(x, h)
        return x

class Decoder(nn.Module):

    def __init__(self):
        super(Decoder, self).__init__()
        self.transformer = nn.Transformer(
            d_model=1024+128, nhead=8, num_encoder_layers=2, num_decoder_layers=2, dropout=0.1)
        self.l1 = nn.Linear(1024+128, 142)
    
    def forward(self, image_feature, context_feature, on_cuda = False):
        # image_feature -> [-1, 1024], context_feature -> [-1, seq_size=48, 128]
        image_feature = image_feature.unsqueeze(1)
        # image_feature -> [-1, 1, 1024]
        image_feature = image_feature.repeat(1, context_feature.size(1), 1)
        # image_feature -> [-1, seq_size, 1024]
        x = torch.cat((image_feature, context_feature), 2)
        # x -> [-1, seq_size=48, 1024+128]

        x, _ = self.transformer(x, x)
        x = self.l1(x)
        # x = F.softmax(x, dim=1)
        return x



