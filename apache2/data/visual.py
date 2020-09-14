#!/home/woongsup/anaconda3/bin/python
import sys
import io
import cgi


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type: text/html; charset=utf-8\n")

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
    <style type="text/css">
      #center {
        margin: 0;
      }
    </style>
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
      <li class="nav-item">
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

      <li class="nav-item active">
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

          <!-- Begin Page Content -->
          <div class="container-fluid">

            <!-- Page Heading -->
            <div class="d-sm-flex align-items-center justify-content-between mb-4">
              <h1 class="h3 mb-0 text-gray-800">연도별 가장 많은 진료를 받은 병명 top 10 (국민건강보험 가입자 100만명 기준 )</h1>
            </div>

            <div class="row" id="center">

              <!-- Earnings (Monthly) Card Example -->
              <div class=" mb-4" id='banner1'>
                <button type="button" class="btn btn-outline-primary card border-left-primary shadow h-100 py-2 mr-2" >
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col mr-2">
                        <div class="font-weight-bold text-uppercase mb-1">2014</div>
                      </div>
                      <div class="col-auto">
                        <i class="fas fa-calendar fa-2x text-gray-300"></i>
                      </div>
                    </div>
                  </div>
                </button>
              </div>

              <!-- Earnings (Annual) Card Example -->
              <div class=" mb-4" id='banner2'>
                <button type="button" class="btn btn-outline-success card border-left-success shadow h-100 py-2 mr-2" >
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col mr-2">
                        <div class="font-weight-bold text-uppercase mb-1">2015</a></div>
                      </div>
                      <div class="col-auto">
                        <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                      </div>
                    </div>
                  </div>
                </button>
              </div>

              <!-- Tasks Card Example -->
              <div class=" mb-4" id='banner3'>
                <button type="button" class="btn btn-outline-info card border-left-info shadow h-100 py-2 mr-2">
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col mr-2">
                        <div class="font-weight-bold text-uppercase mb-1">2016</div>
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

              <!-- Tasks Card Example -->
              <div class=" mb-4" id='banner4'>
                <button type="button" class="btn btn-outline-warning card border-left-warning shadow h-100 py-2 mr-2">
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col mr-2">
                        <div class="font-weight-bold text-uppercase mb-1">2017</div>
                        <div class="row no-gutters align-items-center">
                          <div class="col-auto">
                          </div>
                        </div>
                      </div>
                      <div class="col-auto">
                        <i class="fas fa-comments fa-2x text-gray-300"></i>
                      </div>
                    </div>
                  </div>
                </button>
              </div>

              <!-- Tasks Card Example -->
              <div class=" mb-4" id='banner5'>
                <button type="button" class="btn btn-outline-danger card border-left-danger shadow h-100 py-2 mr-2">
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
                      <div class="col mr-2">
                        <div class="font-weight-bold text-uppercase mb-1">2018</div>
                        <div class="row no-gutters align-items-center">
                          <div class="col-auto">
                          </div>
                        </div>
                      </div>
                      <div class="col-auto">
                        <i class="fas fa-comments fa-2x text-gray-300"></i>
                      </div>
                    </div>
                  </div>
                </button>
              </div>


              

            <p><img src=".//visual//2014.png" width="1300" height="550" id="img"></p>
           

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
          $("p img").attr('src', './visual/2014.png')
      })

      var btn2 = document.getElementById('banner2');
        btn2.addEventListener('click', function(){
          $("p img").attr('src', './visual/2015.png')
      })

      var btn3 = document.getElementById('banner3');
        btn3.addEventListener('click', function(){      
          $("p img").attr('src', './visual/2016.png')
      })

      var btn4 = document.getElementById('banner4');
        btn4.addEventListener('click', function(){
          $("p img").attr('src', './visual/2017.png')
      })

      var btn5 = document.getElementById('banner5');
        btn5.addEventListener('click', function(){
          $("p img").attr('src', './visual/2018.png')
      })  
    </script>

  </body>

  </html>
  '''
  	)
