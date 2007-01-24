# Zeobuilder is an extensible GUI-toolkit for molecular model construction.
# Copyright (C) 2005 Toon Verstraelen
#
# This file is part of Zeobuilder.
#
# Zeobuilder is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# --



from matplotlib import rcParams

rcParams["backend"] = "GTKAgg"
rcParams["numerix"] = "numpy"
rcParams["font.size"] = 9
rcParams["legend.fontsize"] = 8
rcParams["axes.titlesize"] = 9
rcParams["axes.labelsize"] = 9
rcParams["xtick.labelsize"] = 9
rcParams["ytick.labelsize"] = 9
rcParams["figure.facecolor"] = "w"

from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

# UGLY HACK: TODO report this as a bug to the matplotlib project
import gtk
from zeobuilder.gui import load_image
gtk.window_set_default_icon(load_image("zeobuilder.svg"))
# END UGLY HACK