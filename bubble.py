'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px

import hover_template


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The markers' maximum size is 30 and their minimum
        size is 5.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Define figure with animation
    # TODO : Construct the scatter plot
    fig = px.scatter(my_df, x='GDP', y='CO2', animation_frame="Year",
                     animation_group="Country Name", size='Population',
                     color="Continent", log_x=True, log_y=True, size_max=30,
                     range_x=gdp_range, range_y=co2_range,
                     hover_name="Country Name", custom_data=['Population'])
    fig.update_traces(marker_sizemin=5)
    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    # TODO : Set the hover template
    hovertempl = hover_template.get_bubble_hover_template()
    fig.update_traces(hovertemplate=hovertempl)
    for frame in fig.frames:
        for continent in frame["data"]:
            continent["hovertemplate"] = hovertempl
    return fig


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year, and to remove
        the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns
            The updated figure
    '''
    # TODO : Update animation menu

    fig.update_layout(
        sliders=[{'currentvalue': {'prefix': 'Data for Year : '}}],
        updatemenus=[{
            'type': 'buttons',
            'buttons': [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": False},
                                    "fromcurrent": True, "transition": {"duration": 300,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Animate",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                      "mode": "immediate",
                                      "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                    "visible": False
                }
            ]
        }])
    return fig


def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update labels
    fig.update_layout(xaxis_title="GDP per capita ($ USD)",
                      yaxis_title="CO2 emission per capita (metric tonnes)")
    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    # TODO : Update template
    fig.update_layout(template="simple_white")
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update legend
    fig.update_layout(legend={"title": {"text": "Legend"}})
    return fig
