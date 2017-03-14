import seaborn as sns


def ppc_density_plot(y, y_rep):
  """
  Cretes 1D kernel density plot comparing data to samples from posterior.

  Parameters
  ----------
  y : numpy array
    A 1-D numpy array
  y_rep : numpy array
    A 2-D numpy array where rows represent different samples from posterior

  Returns
  -------
  matplotlib axes
  """
  ax = sns.kdeplot(y, color="maroon")

  n = y_rep.shape[0]

  for i in range(n):
    ax = sns.kdeplot(y_rep[i,:], color="maroon", alpha=0.2, linewidth=0.8)

  y_line = sns.plt.Line2D([], [], color='maroon', label='y')
  y_rep_line = sns.plt.Line2D([], [], color='maroon', alpha=0.2, label='y_rep')

  handles = [y_line, y_rep_line]
  labels = ['y', r'$y_{rep}$']

  ax.legend(handles, labels)

  return ax

def ppc_stat_hist_plot(y_stats, yrep_stats, stat_name=None, **kwargs):
  """
  Cretes histogram plot comparing data to samples from posterior.

  Parameters
  ----------
  y_stats : numpy array
    A 1D numpy array
  yrep_stats : float
    Float representing statistic value of observed data
  stat_name : string
    Optional string value for including statistic name in legend
  Keyword Arguments
    Keyword arguments used by seaborn.distplot can be given to customize plot


  Returns
  -------
  matplotlib axes
  """
  ax = sns.distplot(yrep_stats, kde=False, label=r'$T(y_{rep})$', **kwargs)

  max_value = ax.get_ylim()[1]

  sns.plt.vlines(y_stats, ymin=0.0, ymax=max_value, label='T(y)')

  if stat_name is not None:
    sns.plt.legend(title=stat_name)
  else:
    sns.plt.legend()

  return ax
