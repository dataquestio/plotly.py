import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='color',
        parent_name='layout.scene.zaxis.titlefont',
        **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
