from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Mascota, Auto
from ejemplo.forms import Buscar, FamiliarForm, MascotaForm, BuscarCar, AutoForm
from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request,
    'ejemplo/saludar_a.html',
    {'nombre': nombre}
    )

def sumar(request, a, b):
    return render (request,
    'ejemplo/sumar.html',
    {"a": a,
     "b": b,
     "resultado": a + b
    }
    )

def buscar(request):
    lista_de_nombre = ["German","Daniel", "Romero", "Alvaro"]
    query = request.GET['q']

    if query in lista_de_nombre: 
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"

        
    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

  
    
class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
   

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})




class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]







#MASCOTAS



def mostrar_mascotas(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class BuscarMascota(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_mascotas.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas': lista_mascotas})
        return render(request, self.template_name, {"form": form})


class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "tipo":"", "raza":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "tipo":"", "raza":"", "edad":""}
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarMascota(View):
  template_name = 'ejemplo/mascotas.html'
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      mascota.delete()
      mascota = Mascota.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascota})







#AUTOS



def mostrar_autos(request):
  lista_autos = Auto.objects.all()
  return render(request, "ejemplo/autos.html", {"lista_autos": lista_autos})



class BuscarAuto(View):
    form_class = BuscarCar
    template_name = 'ejemplo/buscar_auto.html'
    initial = {"marca":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            marca = form.cleaned_data.get("marca")
            lista_autos = Auto.objects.filter(marca__icontains=marca).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_autos':lista_autos})
        return render(request, self.template_name, {"form": form})



class AltaAuto(View):

    form_class = AutoForm
    template_name = 'ejemplo/alta_auto.html'
    initial = {"marca":"", "modelo":"", "año":"", "kilometros":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el auto {form.cleaned_data.get('marca')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class ActualizarAuto(View):
  form_class = AutoForm
  template_name = 'ejemplo/actualizar_auto.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  
  def get(self, request, pk): 
      auto = get_object_or_404(Auto, pk=pk)
      form = self.form_class(instance=auto)
      return render(request, self.template_name, {'form':form,'auto': auto})


  def post(self, request, pk): 
      auto = get_object_or_404(Auto, pk=pk)
      form = self.form_class(request.POST ,instance=auto)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el auto {form.cleaned_data.get('marca')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'auto': auto,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})




class BorrarAuto(View):
  template_name = 'ejemplo/autos.html'
  
  def get(self, request, pk): 
      auto = get_object_or_404(Auto, pk=pk)
      auto.delete()
      autos = Auto.objects.all()
      return render(request, self.template_name, {'lista_autos': autos})