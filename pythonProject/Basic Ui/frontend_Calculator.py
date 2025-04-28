import wx

def press_addition_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 + number_2))

def press_subtraction_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 - number_2))

def press_multiplication_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 * number_2))

def press_division_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 / number_2))

def press_exponentialPower_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 ** number_2))

def press_floorDivision_button(event):
    number_1 = float(input_1_box.GetValue())
    number_2 = float(input_2_box.GetValue())
    result.SetLabel(str(number_1 // number_2))


app = wx.App()
frame = wx.Frame(parent = None, title = "Calculator")
panel = wx.Panel(frame)
sizer = wx.GridBagSizer()


input_1_label = wx.StaticText(panel, label = "Number 1: ")
input_1_box = wx.TextCtrl(panel)
input_2_label = wx.StaticText(panel, label = "Number 2: ")
input_2_box = wx.TextCtrl(panel)
result_label = wx.StaticText(panel, label = "Result: ")
result = wx.StaticText(panel, label = "")
addition_button = wx.Button(panel, label = "Addition")
addition_button.Bind(wx.EVT_BUTTON, press_addition_button)
subtraction_button = wx.Button(panel, label = "Subtraction")
subtraction_button.Bind(wx.EVT_BUTTON, press_subtraction_button)
multiplication_button = wx.Button(panel, label = "Multiplication")
multiplication_button.Bind(wx.EVT_BUTTON, press_multiplication_button)
division_button = wx.Button(panel, label = "Dividion")
division_button.Bind(wx.EVT_BUTTON, press_division_button)
exponentialPower_button = wx.Button(panel, label = "Exponential Power")
exponentialPower_button.Bind(wx.EVT_BUTTON, press_exponentialPower_button)
floorDivision_button = wx.Button(panel, label = "Floor Division")
floorDivision_button.Bind(wx.EVT_BUTTON, press_floorDivision_button)


sizer.Add(input_1_label, (0, 0))
sizer.Add(input_1_box, (0, 1))
sizer.Add(input_2_label, (1, 0))
sizer.Add(input_2_box, (1, 1))
sizer.Add(result_label, (2, 0))
sizer.Add(result, (2, 1))
sizer.Add(addition_button, (3, 0))
sizer.Add(subtraction_button, (4, 0))
sizer.Add(multiplication_button, (5, 0))
sizer.Add(division_button, (6, 0))
sizer.Add(exponentialPower_button, (7, 0))
sizer.Add(floorDivision_button, (8, 0))


panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)
frame.Show()
app.MainLoop()
