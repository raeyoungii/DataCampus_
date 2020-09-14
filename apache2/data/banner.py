#!/home/woongsup/anaconda3/bin/python
import sys
import io
import cgi
import pandas as pd
from cnt_test import count_plus

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html; charset=utf-8\n")

df = pd.read_csv('./data/total_disease2_count_FINAL.csv', encoding='cp949')

#name값은 병명 매개변수로 받아오기
name = "A형 간염" #default 값은 A형 간염
form = cgi.FieldStorage()
if 'name' in form:
  name = form["name"].value

# count += 1
count_plus(name)

def definition():
    return df.loc[df[df['title'] == name].index[0]]['definition']
    
def cause():
    return df.loc[df[df['title'] == name].index[0]]['cause']

def symptoms():
    return df.loc[df[df['title'] == name].index[0]]['symptoms']

def treatment():
    return df.loc[df[df['title'] == name].index[0]]['treatment']

def progress(): #합병증
    return df.loc[df[df['title'] == name].index[0]]['progress']

def prevention():
    return df.loc[df[df['title'] == name].index[0]]['prevention']

def diagnosis():
    return df.loc[df[df['title'] == name].index[0]]['diagnosis']

print('''

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>증상 설명</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

      <!-- Sidebar - Brand -->
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.py">
        <div class="sidebar-brand-icon rotate-n-15">
          <i class="fas fa-laugh-wink"></i>
        </div>
        <div class="sidebar-brand-text mx-3">어의가 없네</div>
      </a>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">

      <!-- Heading -->
      <div class="sidebar-heading">
        Symptoms
      </div>

      <!-- Nav Item - Dashboard -->
      <li class="nav-item">
        <a class="nav-link" href="index.py">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>증상 입력</span></a>
      </li>

      <!-- Nav Item - Charts -->
      <li class="nav-item">
        <a class="nav-link" href="chart.py">
          <i class="fas fa-fw fa-chart-area"></i>
          <span>증상 예측</span></a>
      </li>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item active">
        <a class="nav-link collapsed" href="banner.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>증상 세부 설명</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider">

      <!-- Heading -->
      <div class="sidebar-heading">
        Data analysis
      </div>
      

      <li class="nav-item">
        <a class="nav-link collapsed" href="usage.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>사용자 이용 현황</span></a>
      </li>

      <li class="nav-item">
        <a class="nav-link collapsed" href="visual.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>의료 데이터 시각화</span></a>
      </li>

      <li class="nav-item">
        <a class="nav-link collapsed" href="map.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>근처 병원 안내</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider d-none d-md-block">

      <!-- Sidebar Toggler (Sidebar) -->
      <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
      </div>

    </ul>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">

        <!-- Topbar -->
        <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

          <!-- Sidebar Toggle (Topbar) -->
          <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
            <i class="fa fa-bars"></i>
          </button>

          <!-- Topbar Search -->
          <form class="d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search" 
          action="banner.py" >
            <div class="input-group">
              <input type="text" class="form-control bg-light border-0 small" placeholder="다른 병명을 검색합니다." 
              
                aria-label="Search" aria-describedby="basic-addon2" name="name">
              <div class="input-group-append">
                
                  <input class="btn btn-primary" type="submit">
                
              </div>
            </div>
          </form>

          <!-- Topbar Navbar -->
          <ul class="navbar-nav ml-auto">

            <!-- Nav Item - Search Dropdown (Visible Only XS) -->
            <li class="nav-item dropdown no-arrow d-sm-none">
              <a class="nav-link dropdown-toggle" href="#" id="searchDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <i class="fas fa-search fa-fw"></i>
              </a>
              <!-- Dropdown - Messages -->
              <div class="dropdown-menu dropdown-menu-right p-3 shadow animated--grow-in" aria-labelledby="searchDropdown">
                <form class="form-inline mr-auto w-100 navbar-search">
                  <div class="input-group">
                    <input type="text" class="form-control bg-light border-0 small" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2">
                    <div class="input-group-append">
                      <button class="btn btn-primary" type="button">
                        <i class="fas fa-search fa-sm"></i>
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </li>

        </nav>
        <!-- End of Topbar -->

        <!-- Begin Page Content -->
        <div class="container-fluid">

          <!-- Page Heading -->
          <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0 text-gray-800"><strong><I>{}</I></strong> 에 대해 알고 싶은 내용을 클릭해주세요.</h1>
        '''.format(name))
print('''
          </div>

          <div class="row">

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner1'>
              <button type="button" class="btn btn-outline-primary card border-left-primary shadow h-100 py-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">정의&원인</div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </button>
            </div>

            <!-- Earnings (Annual) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner2'>
              <button type="button" class="btn btn-outline-success card border-left-success shadow h-100 py-2 col mr-2" >
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">증상&치료법</a></div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </button>
            </div>

            <!-- Tasks Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner3'>
              <button type="button" class="btn btn-outline-info card border-left-info shadow h-100 py-2 mr-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">합병증&예방법</div>
                      <div class="row no-gutters align-items-center">
                        <div class="col-auto">
                        </div>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </button>
            </div>

            <!-- Pending Requests Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner4'>
              <button type="button" class="btn btn-outline-warning card border-left-warning shadow h-100 py-2 mr-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">진단(검사)하는법</div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-comments fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </button>
          </div>

          <div class="row">

            <div class="col-lg-6">

              <!-- Dropdown Card Example -->
              <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                  <h6 class="m-0 font-weight-bold text-primary" id="title1">정의</h6>
                  <div class="dropdown no-arrow">
                    <div class="dropdown-menu dropdown-menu-right shadow animated--fade-in" aria-labelledby="dropdownMenuLink"></div>
                  </div>
                </div>

                <!-- Card Body -->
                <div class="card-body" id='content1'>
                        {}
              '''.format(definition()))
print('''
                </div>
              </div>

            </div>

            <div class="col-lg-6">

              <!-- Dropdown Card Example -->
              <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                  <h6 class="m-0 font-weight-bold text-primary" id='title2'>원인</h6>
                  <div class="dropdown no-arrow">
                    <!-- <a class="dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">이거 이용
                    </a> -->
                    <div class="dropdown-menu dropdown-menu-right shadow animated--fade-in" aria-labelledby="dropdownMenuLink"></div>
                  </div>
                </div>

                <!-- Card Body -->
                <div class="card-body" id='content2'>
                      {}
              '''.format(cause()))
print('''
                </div>
              </div>

            </div>

          </div>

        </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="sticky-footer bg-white">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <strong><span>(법적 한계에 대한 고지) </span></strong>
                <br><br>
                <strong><span>본 정보는 건강정보에 대한 소비자의 이해를 돕기 위한 참고자료일 뿐이며 <br> 개별 환자의 증상과 질병에 대한 정확한 판단을 위해서는 의사의 진료가 반드시 필요합니다.</span></strong>
          </div>
        </div>
      </footer>
      <!-- End of Footer -->

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Logout Modal-->
  <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
          </button>
        </div>
        <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
          <a class="btn btn-primary" href="login.html">Logout</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript-->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin-2.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

  <script>
    var btn1 = document.getElementById('banner1');
    btn1.addEventListener('click', function(){
    ''')
print('''
      $("#title1").html("정의");
      $("#title2").html("원인");  
      $("#content1").html("{}");
      $("#content2").html("{}");
    '''.format(definition(), cause()))
print('''
    })

    var btn2 = document.getElementById('banner2');
    btn2.addEventListener('click', function(){
    ''')
print('''
      $("#title1").html("증상");
      $("#title2").html("치료법");
      $("#content1").html("{}");
      $("#content2").html("{}");
      '''.format(symptoms(), treatment()))
print('''
    })

    var btn3 = document.getElementById('banner3');
    btn3.addEventListener('click', function(){
    ''')
print('''
      $("#title1").html("합병증");
      $("#title2").html("예방법");
      $("#content1").html("{}");
      $("#content2").html("{}");
    '''.format(progress(), prevention()))
print('''
    })

    var btn4 = document.getElementById('banner4');
    btn4.addEventListener('click', function(){
    ''')
print('''
      $("#title1").html("진단법");
      $("#title2").html("");
      $("#content1").html("{}");
      $("#content2").html("");
    '''.format(diagnosis()))
print('''
    })
  </script>

</body>

</html>


'''
  )
