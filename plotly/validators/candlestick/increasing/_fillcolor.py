import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='fillcolor',
        parent_name='candlestick.increasing',
        **kwargs
    ):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'style'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
